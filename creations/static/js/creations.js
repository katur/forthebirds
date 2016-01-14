(function() {
  var initializeImageCaptions, initializeProgramInfoButtons;

  $(document).ready(function() {
    if ($("body").attr("id") === "radio") {
      initializeProgramInfoButtons();
    }
    return initializeImageCaptions();
  });

  initializeProgramInfoButtons = function() {
    var programIntros;
    programIntros = $(".program-intro");
    return programIntros.click(function(e) {
      var program, programMore;
      e.preventDefault();
      $(this).toggleClass("active");
      program = $(this).closest(".program");
      programMore = program.find(".program-more");
      if (programMore.is(":visible")) {
        return programMore.hide();
      } else {
        return programMore.show();
      }
    });
  };

  initializeImageCaptions = function() {
    var altText, i, image, len, markdownImages, results, title;
    markdownImages = $(".markdown img");
    results = [];
    for (i = 0, len = markdownImages.length; i < len; i++) {
      image = markdownImages[i];
      altText = $(image).attr("alt");
      if ((altText.indexOf("BANNER")) !== -1) {
        $(image).wrap('<div class="image-wrapper banner">');
      } else {
        $(image).wrap('<div class="image-wrapper">');
      }
      title = $(image).attr("title");
      if (title) {
        results.push($(image).after("<span class=\"image-caption\">" + title + "</span>"));
      } else {
        results.push(void 0);
      }
    }
    return results;
  };

}).call(this);
