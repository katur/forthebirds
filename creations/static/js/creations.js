(function() {
  var addArtworkToElement, addRadioProgramArtwork, addSoundRecordingArtwork, initializeImageCaptions, initializeProgramButtons, watchYearSelect;

  $(document).ready(function() {
    var page;
    page = $("body").attr("id");
    if (page === "radio-program") {
      addRadioProgramArtwork();
    }
    if (page === "sound-recording") {
      addSoundRecordingArtwork();
    }
    if (page === "radio") {
      initializeProgramButtons();
      watchYearSelect();
    }
    return initializeImageCaptions();
  });

  addArtworkToElement = function(pk, element, urlStart) {
    return $.ajax("/" + urlStart + "/artwork/" + pk + "/", {
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

  addRadioProgramArtwork = function() {
    var artworkElement, pk;
    artworkElement = $("#artwork");
    pk = artworkElement.attr("data-pk");
    return addArtworkToElement(pk, artworkElement, "radio");
  };

  addSoundRecordingArtwork = function() {
    var artworkElement, pk;
    artworkElement = $("#artwork");
    pk = artworkElement.attr("data-pk");
    return addArtworkToElement(pk, artworkElement, "sound-recording");
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
      return addArtworkToElement(programPk, artworkElement, "radio");
    });
  };

  watchYearSelect = function() {
    return $("#year-selector").on("change", (function(_this) {
      return function(e) {
        return window.location = "?year=" + ($(e.currentTarget).val());
      };
    })(this));
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
