$(document).ready(function() {
  createRadioYearButtons();
  createProgramInfoButtons();
});

createRadioYearButtons = function() {
  yearButtons = $(".year-button");
  yearPrograms = $(".year-programs");

  yearButtons.on("click", function(e) {
    e.preventDefault();
    yearButtons.removeClass("active");
    yearPrograms.css("display", "none");

    year = $(this).attr("id");
    $(this).addClass("active");
    $("#" + year + ".year-programs").css("display", "block");
  });

  $(".year-button:first").click();
}

createProgramInfoButtons = function() {
  programInfoButtons = $(".program-info-button");
  programInfoBoxes = $(".program-info");

  programInfoButtons.on("click", function(e) {
    e.preventDefault();
    program = $(this).closest(".program");
    programInfo = program.find(".program-info");

    $(this).toggleClass("active");
    if ($(this).hasClass("active")) {
      programInfo.css("display", "block");
    } else {
      programInfo.css("display", "none");
    }
  });
}
