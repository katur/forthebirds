$(document).ready(function() {
  createExpandButtons();
});

createExpandButtons = function() {
  links = $(".plus-sign").closest("a");

  links.css("cursor", "pointer");

  links.on("click", function(e) {
    e.preventDefault();
    $(this).toggleClass("active");
    $(this).find(".plus-sign").toggleClass("minus");
    $(this).closest("li").next("ul").toggleClass("collapsed");
  });
}
