$(document).ready(function() {
  if ($("body").attr("id") === "ways-to-help") {
    generateRandomBackgroundColors();
    generateBackgroundImagesForWays();
  }
});


function generateRandomBackgroundColors() {
  var elements = $(".random-background-color");
  var results = [];

  var i, element, hash, hexString;
  for (i = 0; i < elements.length; i++) {
    element = $(elements[i]);
    hash = getHexableHash(element.text());
    hexString = hash.toString(16);
    results.push(element.css("background-color", "#" + hexString));
  }

  return results;
};


const NUM_HEX_COLORS = Math.pow(2, 4 * 6);


function getHexableHash(str) {
  var hash = getHashCode(str);
  var r = hash % NUM_HEX_COLORS;

  if (r < 0) {
    r *= -1;
  }

  return r;
};


function getHashCode(str) {
  var hash = 0;

  if (str.length === 0) {
    return hash;
  }

  var i, ch;
  for (i = 0; i < str.length; i++) {
    ch = str[i];
    if (ch.trim() === "") {
      continue;
    }
    hash = ((hash << 5) - hash) + ch.charCodeAt(0);
    hash |= 0;
  }

  return hash;
};


function generateBackgroundImagesForWays() {
  var ways = $(".way-to-help-card");
  var results = [];

  var i, j, way, backgroundImage;
  for (i = 0, j = ways.length; i < j; i++) {
    way = $(ways[i]);
    backgroundImage = way.attr("data-background");
    results.push(way.css("background-image", "url(" + backgroundImage + ")"));
  }

  return results;
};
