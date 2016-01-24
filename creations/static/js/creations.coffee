$(document).ready ->
  if $("body").attr("id") == "radio-program"
    addArtwork()

  if $("body").attr("id") == "radio"
    initializeProgramButtons()

  initializeImageCaptions()


addRadioProgramArtworkToElement = (radioProgramPk, element) ->
  $.ajax "/radio/program-artwork/#{radioProgramPk}/",
    type: "GET"
    dataType: "json"
    success: (data, textStatus, jqXHR) ->
      if data.artwork
        src = "data:image;base64,#{data.artwork}"
        element.html("""<img src="#{src}"/>""")


addArtwork = ->
  artworkElement = $("#artwork")
  programPk = artworkElement.attr("data-program-pk")
  addRadioProgramArtworkToElement(programPk, artworkElement)


initializeProgramButtons = ->
  programIntros = $(".program-intro")

  programIntros.click (e) ->
    e.preventDefault()
    $(this).toggleClass("active")

    program = $(this).closest(".program")
    programMore = program.find(".program-more")

    if (programMore.is(":visible"))
      programMore.hide()
    else
      programMore.show()

    programPk = program.attr("data-program-pk")
    artworkElement = program.find(".artwork")
    addRadioProgramArtworkToElement(programPk, artworkElement)


initializeImageCaptions = ->
  markdownImages = $(".markdown img")

  for image in markdownImages
    altText = $(image).attr("alt")

    if ((altText.indexOf "BANNER") isnt -1)
      $(image).wrap('<div class="image-wrapper banner">')
    else
      $(image).wrap('<div class="image-wrapper">')

    title = $(image).attr("title")
    if title
      $(image).after("""<span class="image-caption">#{title}</span>""")
