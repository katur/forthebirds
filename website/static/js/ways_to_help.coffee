$(document).ready ->
  generateBackgroundColorsForWays()


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


generateBackgroundColorsForWays = ->
  ways = $(".way-to-help-card")
  for way in ways
    way = $(way)
    text = way.text()
    hash = getHexableHash(text)
    hexString = hash.toString(16)
    way.css("background-color", "#" + hexString)
