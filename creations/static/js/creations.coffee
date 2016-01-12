$(document).ready ->
  if $("body").attr("id") == "radio"
    initializeProgramInfoButtons()

  initializeImageCaptions()


initializeProgramInfoButtons = ->
  programIntros = $(".program-intro")

  programIntros.click (e) ->
    e.preventDefault()

    program = $(this).closest(".program")
    programMore = program.find(".program-more")

    if (programMore.is(":visible"))
      programMore.hide()
    else
      programMore.show()


initializeImageCaptions = ->
  markdownImages = $(".markdown img")

  for image in markdownImages
    altText = $(image).attr("alt")
    if "BANNER" in altText
      $(image).wrap('<div class="image-wrapper banner">')
    else
      $(image).wrap('<div class="image-wrapper">')
      $(image).after("""<span class="image-caption">#{altText}</span>""")
