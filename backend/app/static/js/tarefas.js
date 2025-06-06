// Função para atualizar a URL com os parâmetros de filtro
function updateFilterUrl(select) {
  const params = new URLSearchParams(window.location.search);

  if (select.value) {
    params.set('user_id', select.value);
  } else {
    params.delete('user_id');
  }

  window.location.href = `${window.location.pathname}?${params.toString()}`;
}

// Inicializa os tooltips do Bootstrap
document.addEventListener('DOMContentLoaded', function () {
  var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
});
