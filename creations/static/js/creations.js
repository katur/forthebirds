$(document).ready(function() {
  initializeRadioYearButtons();
  initializeProgramInfoButtons();
});

initializeRadioYearButtons = function() {
  yearButtons = $(".year-button");
  yearPrograms = $(".year-programs");

  yearButtons.on("click", function(e) {
    e.preventDefault();
    yearButtons.removeClass("active");
    yearPrograms.hide();
    $(".program-info").hide();

    year = $(this).attr("id");
    $(this).addClass("active");
    $("#" + year + ".year-programs").show();
  });

  $(".year-button:first").click();
}

initializeProgramInfoButtons = function() {
  programInfoButtons = $(".program-info-button");
  programInfoBoxes = $(".program-info");

  programInfoButtons.on("click", function(e) {
    e.preventDefault();

    program = $(this).closest(".program");
    programInfo = program.find(".program-info");

    if (programInfo.is(":visible")) {
      programInfo.hide();
    } else {
      programInfo.show();
    }
  });
}
