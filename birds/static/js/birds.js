$(document).ready(function() {
  createExpandButtons();
});

createExpandButtons = function() {
  $(".plus-sign").closest("li").on("click", function() {
    $(this).find(".plus-sign").toggleClass("minus");
    $(this).next("ul").toggleClass("collapsed");
  });
}
