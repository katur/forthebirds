$(document).ready ->
  if $("body").attr("id") == "ways-to-help"
    generateRandomBackgroundColors()
    generateBackgroundImagesForWays()


generateBackgroundImagesForWays = ->
  ways = $(".way-to-help-card")
  for way in ways
    way = $(way)
    backgroundImage = way.attr("data-background")
    way.css("background-image", "url(" + backgroundImage + ")")


getHashCode = (str) ->
  hash = 0
  len = str.length

  if (len == 0)
    return hash

  for char in str
    continue if char.trim() == ""
    code = char.charCodeAt(0)
    hash = ((hash << 5) - hash) + code
    hashPrev = hash
    hash |= 0 # Convert to 32-bit integer

  return hash


numHexColors = Math.pow(2, 4*6)


getHexableHash = (str) ->
  hash = getHashCode(str)
  i = hash % numHexColors
  if i < 0
    i *= -1
  return i


generateRandomBackgroundColors = ->
  elements = $(".random-background-color")
  for element in elements
    element = $(element)
    text = element.text()
    hash = getHexableHash(text)
    hexString = hash.toString(16)
    element.css("background-color", "#" + hexString)
