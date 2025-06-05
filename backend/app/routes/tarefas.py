from flask import Blueprint, request, session, redirect, url_for, render_template, current_app, flash
from .auth import login_required, admin_required
from datetime import datetime

bp = Blueprint('tarefas', __name__, url_prefix='/tarefas')

def parse_datetime(datetime_str):
    """Tenta converter uma string de data/hora em vários formatos possíveis."""
    formatos = [
        '%Y-%m-%d %H:%M:%S',  # Formato completo com segundos
        '%Y-%m-%d %H:%M',     # Formato sem segundos
        '%Y-%m-%dT%H:%M',     # Formato ISO
        '%Y-%m-%dT%H:%M:%S'   # Formato ISO com segundos
    ]
    
    for formato in formatos:
        try:
            return datetime.strptime(datetime_str, formato)
        except ValueError:
            continue
    
    raise ValueError(f"Formato de data/hora inválido: {datetime_str}")

def verificar_prazo(db, tarefa_id):
    """Verifica se uma tarefa está atrasada e atualiza seu status se necessário."""
    tarefa = db.execute('''
        SELECT id, horario, status 
        FROM tarefa 
        WHERE id = ? AND status = 'aprovada' AND horario IS NOT NULL
    ''', (tarefa_id,)).fetchone()
    
    if tarefa and tarefa['horario']:
        try:
            prazo = parse_datetime(tarefa['horario'])
            agora = datetime.now()
            
            if agora > prazo:
                db.execute('''
                    UPDATE tarefa 
                    SET status = 'atrasada',
                        updated_at = datetime('now', '-3 hours')
                    WHERE id = ?
                ''', (tarefa_id,))
                db.commit()
                return True
        except ValueError as e:
            current_app.logger.error(f"Erro ao processar data da tarefa {tarefa_id}: {e}")
    return False

def verificar_todas_tarefas(db, familia_id):
    """Verifica todas as tarefas ativas da família quanto a atrasos."""
    tarefas = db.execute('''
        SELECT id 
        FROM tarefa 
        WHERE familia_id = ? AND status = 'aprovada' AND horario IS NOT NULL
    ''', (familia_id,)).fetchall()
    
    for tarefa in tarefas:
        verificar_prazo(db, tarefa['id'])

@bp.route('/')
@login_required
def list_tasks():
    db = current_app.get_db()
    
    # Verifica tarefas atrasadas antes de listar
    verificar_todas_tarefas(db, session['family_id'])
    
    # Se for admin e o parâmetro all=true, mostra todas as tarefas ativas da família
    show_all = session.get('is_admin') and request.args.get('all') == 'true'
    
    if show_all:
        tasks = db.execute('''
            SELECT 
                t.*,
                u1.nome as criador_nome,
                u2.nome as responsavel_nome,
                datetime(t.created_at, '-3 hours') as created_at,
                datetime(t.updated_at, '-3 hours') as updated_at
            FROM tarefa t
            JOIN usuario u1 ON t.criador_id = u1.id
            JOIN usuario u2 ON t.destinatario_id = u2.id
            WHERE u1.familia_id = ? 
            AND t.status IN ('aprovada', 'atrasada', 'pendente')
            ORDER BY 
                CASE 
                    WHEN t.status = 'atrasada' THEN 1
                    WHEN t.status = 'aprovada' THEN 2
                    WHEN t.status = 'pendente' THEN 3
                    ELSE 4
                END,
                t.created_at DESC
        ''', (session['family_id'],)).fetchall()
    else:
        # Mostra apenas tarefas ativas atribuídas ao usuário
        tasks = db.execute('''
            SELECT 
                t.*,
                u1.nome as criador_nome,
                u2.nome as responsavel_nome,
                datetime(t.created_at, '-3 hours') as created_at,
                datetime(t.updated_at, '-3 hours') as updated_at
            FROM tarefa t
            JOIN usuario u1 ON t.criador_id = u1.id
            JOIN usuario u2 ON t.destinatario_id = u2.id
            WHERE t.destinatario_id = ? 
            AND t.status IN ('aprovada', 'atrasada', 'pendente')
            ORDER BY 
                CASE 
                    WHEN t.status = 'atrasada' THEN 1
                    WHEN t.status = 'aprovada' THEN 2
                    WHEN t.status = 'pendente' THEN 3
                    ELSE 4
                END,
                t.created_at DESC
        ''', (session['user_id'],)).fetchall()
    
    return render_template('tarefas/list.html', tasks=tasks, show_all=show_all)

@bp.route('/history')
@login_required
def history():
    db = current_app.get_db()
    
    status_filter = request.args.get('status', 'all')
    status_conditions = {
        'pendentes': "t.status = 'pendente'",
        'atrasadas': "t.status = 'atrasada'",
        'rejeitadas': "t.status = 'rejeitada'",
        'concluidas': "t.status = 'concluida'",
        'all': "1=1"
    }
    status_condition = status_conditions.get(status_filter, "1=1")
    
    # Se for admin, mostra histórico de toda a família
    if session.get('is_admin'):
        tasks = db.execute(f'''
            SELECT 
                t.*,
                u1.nome as criador_nome,
                u2.nome as responsavel_nome,
                datetime(t.created_at, '-3 hours') as created_at,
                datetime(t.updated_at, '-3 hours') as updated_at
            FROM tarefa t
            JOIN usuario u1 ON t.criador_id = u1.id
            JOIN usuario u2 ON t.destinatario_id = u2.id
            WHERE u1.familia_id = ? AND {status_condition}
            ORDER BY t.updated_at DESC NULLS LAST, t.created_at DESC
        ''', (session['family_id'],)).fetchall()
    else:
        # Mostra apenas histórico do usuário
        tasks = db.execute(f'''
            SELECT 
                t.*,
                u1.nome as criador_nome,
                u2.nome as responsavel_nome,
                datetime(t.created_at, '-3 hours') as created_at,
                datetime(t.updated_at, '-3 hours') as updated_at
            FROM tarefa t
            JOIN usuario u1 ON t.criador_id = u1.id
            JOIN usuario u2 ON t.destinatario_id = u2.id
            WHERE t.destinatario_id = ? AND {status_condition}
            ORDER BY t.updated_at DESC NULLS LAST, t.created_at DESC
        ''', (session['user_id'],)).fetchall()
    
    return render_template('tarefas/history.html', 
                         tasks=tasks, 
                         current_status=status_filter)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_task():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form.get('descricao')
        destinatario_id = request.form['destinatario_id']
        horario = request.form.get('horario')  # Formato: YYYY-MM-DDTHH:MM
        
        if horario:
            # Converte o formato datetime-local para o formato do banco
            horario = horario.replace('T', ' ')
        
        db = current_app.get_db()
        error = None
        
        if not titulo:
            error = 'Título é obrigatório.'
        elif not destinatario_id:
            error = 'Responsável é obrigatório.'
            
        # Verifica se o usuário atribuído pertence à mesma família
        if error is None:
            user = db.execute(
                'SELECT * FROM usuario WHERE id = ? AND familia_id = ?',
                (destinatario_id, session['family_id'])
            ).fetchone()
            if user is None:
                error = 'Usuário inválido.'
        
        if error is None:
            # Se não for admin, cria como pendente
            status = 'aprovada' if session.get('is_admin') else 'pendente'
            
            db.execute('''
                INSERT INTO tarefa (
                    titulo, descricao, destinatario_id, criador_id, 
                    horario, status, familia_id, created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now', '-3 hours'))
            ''', (titulo, descricao, destinatario_id, session['user_id'], 
                  horario, status, session['family_id']))
            db.commit()
            
            flash('Tarefa criada com sucesso!')
            return redirect(url_for('tarefas.list_tasks'))
            
        flash(error)
    
    # Obtém lista de membros da família para o select
    db = current_app.get_db()
    membros = db.execute(
        'SELECT id, nome FROM usuario WHERE familia_id = ?',
        (session['family_id'],)
    ).fetchall()
    
    return render_template('tarefas/create.html', membros=membros)

@bp.route('/<int:id>/complete', methods=['POST'])
@login_required
def complete_task(id):
    db = current_app.get_db()
    
    # Verifica se a tarefa pertence ao usuário e está ativa ou atrasada
    task = db.execute('''
        SELECT * FROM tarefa 
        WHERE id = ? AND destinatario_id = ? 
        AND status IN ('aprovada', 'atrasada')
    ''', (id, session['user_id'])).fetchone()
    
    if task is None:
        flash('Tarefa não encontrada ou você não tem permissão.')
    else:
        # Verifica se está atrasada antes de concluir
        verificar_prazo(db, id)
        task = db.execute('SELECT * FROM tarefa WHERE id = ?', (id,)).fetchone()
        
        # Se estiver atrasada, exige justificativa
        if task['status'] == 'atrasada':
            justificativa = request.form.get('justificativa_atraso')
            if not justificativa:
                flash('É necessário fornecer uma justificativa para concluir uma tarefa atrasada.', 'error')
                return redirect(url_for('tarefas.list_tasks'))
        else:
            justificativa = None
        
        # Atualiza o status para concluída
        db.execute('''
            UPDATE tarefa 
            SET status = 'concluida',
                justificativa = COALESCE(?, justificativa),
                updated_at = datetime('now', '-3 hours')
            WHERE id = ?
        ''', (justificativa, id))
        db.commit()
        
        if task['status'] == 'atrasada':
            flash('Tarefa concluída com atraso. Justificativa registrada.')
        else:
            flash('Tarefa marcada como concluída.')
    
    return redirect(url_for('tarefas.list_tasks'))

@bp.route('/<int:id>/approve', methods=['POST'])
@admin_required
def approve_task(id):
    db = current_app.get_db()
    
    # Verifica se a tarefa pertence à família do admin
    task = db.execute('''
        SELECT t.* FROM tarefa t
        JOIN usuario u ON t.destinatario_id = u.id
        WHERE t.id = ? AND u.familia_id = ?
    ''', (id, session['family_id'])).fetchone()
    
    if task is None:
        flash('Tarefa não encontrada.')
    else:
        db.execute(
            "UPDATE tarefa SET status = 'aprovada', updated_at = datetime('now', '-3 hours') WHERE id = ?",
            (id,)
        )
        db.commit()
        flash('Tarefa aprovada.')
    
    return redirect(url_for('tarefas.list_tasks', all='true'))

@bp.route('/<int:id>/reject', methods=['POST'])
@login_required
def reject_task(id):
    db = current_app.get_db()
    justificativa = request.form.get('justificativa')
    
    # Verifica se a tarefa pertence à família e se o usuário tem permissão
    task = db.execute('''
        SELECT t.* FROM tarefa t
        JOIN usuario u ON t.destinatario_id = u.id
        WHERE t.id = ? AND (
            (t.destinatario_id = ? AND t.status IN ('aprovada', 'atrasada')) OR 
            (u.familia_id = ? AND ? = 1)
        )
    ''', (id, session['user_id'], session['family_id'], session['is_admin'])).fetchone()
    
    if task is None:
        flash('Tarefa não encontrada ou você não tem permissão.', 'error')
    elif not justificativa:
        flash('É necessário fornecer uma justificativa para rejeitar a tarefa.', 'error')
    else:
        db.execute('''
            UPDATE tarefa 
            SET status = 'rejeitada', 
                updated_at = datetime('now', '-3 hours'),
                justificativa = ?
            WHERE id = ?
        ''', (justificativa, id))
        db.commit()
        flash('Tarefa rejeitada com sucesso.', 'success')
    
    if session.get('is_admin'):
        return redirect(url_for('tarefas.list_tasks', all='true'))
    return redirect(url_for('tarefas.list_tasks'))

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    db = current_app.get_db()
    
    # Busca a tarefa e verifica permissões
    task = db.execute('''
        SELECT t.*, u1.nome as criador_nome, u2.nome as responsavel_nome
        FROM tarefa t
        JOIN usuario u1 ON t.criador_id = u1.id
        JOIN usuario u2 ON t.destinatario_id = u2.id
        WHERE t.id = ? AND (t.criador_id = ? OR ? = 1)
        AND t.familia_id = ?
    ''', (id, session['user_id'], session['is_admin'], session['family_id'])).fetchone()
    
    if task is None:
        flash('Tarefa não encontrada ou você não tem permissão para editá-la.', 'error')
        return redirect(url_for('tarefas.list_tasks'))
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form.get('descricao')
        destinatario_id = request.form['destinatario_id']
        horario = request.form.get('horario')  # Formato: YYYY-MM-DDTHH:MM
        
        if horario:
            # Converte o formato datetime-local para o formato do banco
            horario = horario.replace('T', ' ')
            
            # Verifica se o novo prazo é futuro e a tarefa está atrasada
            try:
                novo_prazo = datetime.strptime(horario, '%Y-%m-%d %H:%M')
                if task['status'] == 'atrasada' and novo_prazo > datetime.now():
                    # Se o novo prazo é futuro, volta para 'aprovada'
                    novo_status = 'aprovada'
                    flash('Prazo atualizado. Tarefa voltou para status "Em andamento".', 'success')
                else:
                    novo_status = task['status']
            except ValueError:
                novo_status = task['status']
        else:
            novo_status = task['status']
        
        error = None
        
        if not titulo:
            error = 'Título é obrigatório.'
        elif not destinatario_id:
            error = 'Responsável é obrigatório.'
            
        # Verifica se o usuário atribuído pertence à mesma família
        if error is None:
            user = db.execute(
                'SELECT * FROM usuario WHERE id = ? AND familia_id = ?',
                (destinatario_id, session['family_id'])
            ).fetchone()
            if user is None:
                error = 'Usuário inválido.'
        
        if error is None:
            db.execute('''
                UPDATE tarefa 
                SET titulo = ?, 
                    descricao = ?, 
                    destinatario_id = ?, 
                    horario = ?,
                    status = ?,
                    updated_at = datetime('now', '-3 hours')
                WHERE id = ?
            ''', (titulo, descricao, destinatario_id, horario, novo_status, id))
            db.commit()
            
            flash('Tarefa atualizada com sucesso!', 'success')
            return redirect(url_for('tarefas.list_tasks'))
            
        flash(error, 'error')
    
    # Obtém lista de membros da família para o select
    membros = db.execute(
        'SELECT id, nome FROM usuario WHERE familia_id = ?',
        (session['family_id'],)
    ).fetchall()
    
    return render_template('tarefas/edit.html', task=task, membros=membros) 