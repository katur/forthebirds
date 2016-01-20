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
      var program, programArtwork, programMore, programPk;
      e.preventDefault();
      $(this).toggleClass("active");
      program = $(this).closest(".program");
      programPk = program.attr("data-program-pk");
      programArtwork = program.find(".artwork");
      programMore = program.find(".program-more");
      if (programMore.is(":visible")) {
        programMore.hide();
      } else {
        programMore.show();
      }
      return $.ajax("/radio/program-artwork/" + programPk + "/", {
        type: 'GET',
        dataType: "json",
        success: function(data, textStatus, jqXHR) {
          var src;
          if (data.artwork) {
            src = "data:image;base64," + data.artwork;
            return programArtwork.html("<img src=\"" + src + "\"/>");
          }
        }
      });
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
