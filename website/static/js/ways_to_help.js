(function() {
  var generateBackgroundColorsForWays, getHashCode, getHexableHash, numHexColors;

  $(document).ready(function() {
    return generateBackgroundColorsForWays();
  });

  getHashCode = function(str) {
    var char, code, hash, hashPrev, j, len, len1;
    hash = 0;
    len = str.length;
    if (len === 0) {
      return hash;
    }
    for (j = 0, len1 = str.length; j < len1; j++) {
      char = str[j];
      if (char.trim() === "") {
        continue;
      }
      code = char.charCodeAt(0);
      hash = ((hash << 5) - hash) + code;
      hashPrev = hash;
      hash |= 0;
    }
    return hash;
  };

  numHexColors = Math.pow(2, 4 * 6);

  getHexableHash = function(str) {
    var hash, i;
    hash = getHashCode(str);
    i = hash % numHexColors;
    if (i < 0) {
      i *= -1;
    }
    return i;
  };

  generateBackgroundColorsForWays = function() {
    var hash, hexString, j, len1, results, text, way, ways;
    ways = $(".way-to-help-card");
    results = [];
    for (j = 0, len1 = ways.length; j < len1; j++) {
      way = ways[j];
      way = $(way);
      text = way.text();
      hash = getHexableHash(text);
      hexString = hash.toString(16);
      results.push(way.css("background-color", "#" + hexString));
    }
    return results;
  };

}).call(this);
