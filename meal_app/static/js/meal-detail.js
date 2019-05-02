$('#meal-detail').bind('keypress', function(event) {
  if(event.which === 13) {
    $(this).next().focus();
  }
});
