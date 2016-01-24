(function() {
  var addArtwork, addRadioProgramArtworkToElement, initializeImageCaptions, initializeProgramButtons;

  $(document).ready(function() {
    if ($("body").attr("id") === "radio-program") {
      addArtwork();
    }
    if ($("body").attr("id") === "radio") {
      initializeProgramButtons();
    }
    return initializeImageCaptions();
  });

  addRadioProgramArtworkToElement = function(radioProgramPk, element) {
    return $.ajax("/radio/program-artwork/" + radioProgramPk + "/", {
      type: "GET",
      dataType: "json",
      success: function(data, textStatus, jqXHR) {
        var src;
        if (data.artwork) {
          src = "data:image;base64," + data.artwork;
          return element.html("<img src=\"" + src + "\"/>");
        }
      }
    });
  };

  addArtwork = function() {
    var artworkElement, programPk;
    artworkElement = $("#artwork");
    programPk = artworkElement.attr("data-program-pk");
    return addRadioProgramArtworkToElement(programPk, artworkElement);
  };

  initializeProgramButtons = function() {
    var programIntros;
    programIntros = $(".program-intro");
    return programIntros.click(function(e) {
      var artworkElement, program, programMore, programPk;
      e.preventDefault();
      $(this).toggleClass("active");
      program = $(this).closest(".program");
      programMore = program.find(".program-more");
      if (programMore.is(":visible")) {
        programMore.hide();
      } else {
        programMore.show();
      }
      programPk = program.attr("data-program-pk");
      artworkElement = program.find(".artwork");
      return addRadioProgramArtworkToElement(programPk, artworkElement);
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
