from flask import Blueprint, request, session, redirect, url_for, render_template, current_app, flash
from .auth import login_required, admin_required

bp = Blueprint('tarefas', __name__, url_prefix='/tarefas')

@bp.route('/')
@login_required
def list_tasks():
    db = current_app.get_db()
    
    # Se for admin e o parâmetro all=true, mostra todas as tarefas da família
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
            WHERE u1.familia_id = ? AND t.status != 'concluida'
            ORDER BY t.created_at DESC
        ''', (session['family_id'],)).fetchall()
    else:
        # Mostra apenas tarefas atribuídas ao usuário
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
            WHERE t.destinatario_id = ? AND t.status != 'concluida'
            ORDER BY t.created_at DESC
        ''', (session['user_id'],)).fetchall()
    
    return render_template('tarefas/list.html', tasks=tasks, show_all=show_all)

@bp.route('/history')
@login_required
def history():
    db = current_app.get_db()
    
    status_filter = request.args.get('status', 'all')
    status_conditions = {
        'pendentes': "t.status = 'pendente'",
        'ativas': "t.status = 'aprovada'",
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
            ORDER BY t.created_at DESC
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
            ORDER BY t.created_at DESC
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
        horario = request.form.get('horario')  # opcional
        
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
    
    # Verifica se a tarefa pertence ao usuário
    task = db.execute(
        'SELECT * FROM tarefa WHERE id = ? AND destinatario_id = ?',
        (id, session['user_id'])
    ).fetchone()
    
    if task is None:
        flash('Tarefa não encontrada ou você não tem permissão.')
    else:
        db.execute(
            "UPDATE tarefa SET status = 'concluida', updated_at = datetime('now', '-3 hours') WHERE id = ?",
            (id,)
        )
        db.commit()
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
            (t.destinatario_id = ? AND t.status = 'aprovada') OR 
            (u.familia_id = ? AND ? = 1)
        )
    ''', (id, session['user_id'], session['family_id'], session['is_admin'])).fetchone()
    
    if task is None:
        flash('Tarefa não encontrada ou você não tem permissão.', 'error')
    elif not session.get('is_admin') and not justificativa:
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
        horario = request.form.get('horario')  # opcional
        
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
                    updated_at = datetime('now', '-3 hours')
                WHERE id = ?
            ''', (titulo, descricao, destinatario_id, horario, id))
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