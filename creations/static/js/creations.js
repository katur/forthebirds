(function() {
  var initializeProgramInfoButtons;

  $(document).ready(function() {
    if ($("body").attr("id") === "radio") {
      return initializeProgramInfoButtons();
    }
  });

  initializeProgramInfoButtons = function() {
    var programIntros;
    programIntros = $(".program-intro");
    return programIntros.click(function(e) {
      var program, programMore;
      e.preventDefault();
      program = $(this).closest(".program");
      programMore = program.find(".program-more");
      if (programMore.is(":visible")) {
        return programMore.hide();
      } else {
        return programMore.show();
      }
    });
  };

}).call(this);
