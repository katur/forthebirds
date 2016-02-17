$(document).ready(function() {
  var page = $("body").attr("id");

  if (page === "radio") {
    watchYearSelect();
    initializeProgramButtons();
  } else if (page === "radio-program") {
    addRadioProgramArtwork();
  } else if (page === "radio-calendar") {
    addCalendarKeyboardNav();
  } else if (page === "sound-recording") {
    addSoundRecordingArtwork();
  }

  initializeImageCaptions();
});


function watchYearSelect() {
  $("#year-selector").on("change", function(e) {
    window.location = "?year=" + ($(e.currentTarget).val());
  });
};


function initializeProgramButtons() {
  $(".program-intro").click(function(e) {
    e.preventDefault();
    $(this).toggleClass("active");

    var program = $(this).closest(".program");
    var programMore = program.find(".program-more");
    var programPk = program.attr("data-program-pk");
    var artworkElement = program.find(".artwork");

    if (programMore.is(":visible")) {
      programMore.hide();
    } else {
      programMore.show();
    }

    addArtworkToElement(programPk, artworkElement, "radio");
  });
};


function addRadioProgramArtwork() {
  var artworkElement = $("#artwork");
  var pk = artworkElement.attr("data-pk");
  addArtworkToElement(pk, artworkElement, "radio");
};


function addArtworkToElement(pk, element, urlStart) {
  $.ajax("/" + urlStart + "/artwork/" + pk + "/", {
    type: "GET",
    dataType: "json",
    success: function(data, textStatus, jqXHR) {
      if (data.artwork) {
        var src = "data:image;base64," + data.artwork;
        element.html("<img src=\"" + src + "\"/>");
      }
    }
  });
};


function addCalendarKeyboardNav() {
  var previous = $("#previous-month");
  var next = $("#next-month");
  $("body").on("keydown", function(e) {
    if (e.which === 37) {
      window.location = previous.attr("href");
    } else if (e.which === 39) {
      window.location = next.attr("href");
    }
  });
};


function addSoundRecordingArtwork() {
  var artworkElement = $("#artwork");
  var pk = artworkElement.attr("data-pk");
  addArtworkToElement(pk, artworkElement, "sound-recording");
};


function initializeImageCaptions() {
  var markdownImages = $(".markdown img");

  var i, image, altText, title;
  for (i = 0; i < markdownImages.length; i++) {
    image = markdownImages[i];
    altText = $(image).attr("alt");

    if ((altText.indexOf("BANNER")) !== -1) {
      $(image).wrap('<div class="image-wrapper banner">');
    } else {
      $(image).wrap('<div class="image-wrapper">');
    }

    title = $(image).attr("title");
    if (title) {
      $(image).after("<span class=\"image-caption\">" + title + "</span>");
    }
  }
};
