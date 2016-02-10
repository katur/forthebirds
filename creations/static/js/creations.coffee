$(document).ready ->
  page = $("body").attr("id")

  if page == "radio"
    initializeProgramButtons()
    watchYearSelect()

  if page == "radio-calendar"
    addCalendarKeyboardNav()

  if page == "radio-program"
    addRadioProgramArtwork()

  if page == "sound-recording"
    addSoundRecordingArtwork()

  initializeImageCaptions()


addCalendarKeyboardNav = ->
  previous = $("#previous-month")
  next = $("#next-month")

  $("body").on("keydown", (e) ->
    if e.which == 37
      window.location = previous.attr("href")
    else if e.which == 39
      window.location = next.attr("href")
  )


addArtworkToElement = (pk, element, urlStart) ->
  $.ajax "/#{urlStart}/artwork/#{pk}/",
    type: "GET"
    dataType: "json"
    success: (data, textStatus, jqXHR) ->
      if data.artwork
        src = "data:image;base64,#{data.artwork}"
        element.html("""<img src="#{src}"/>""")


addRadioProgramArtwork = ->
  artworkElement = $("#artwork")
  pk = artworkElement.attr("data-pk")
  addArtworkToElement(pk, artworkElement, "radio")


addSoundRecordingArtwork = ->
  artworkElement = $("#artwork")
  pk = artworkElement.attr("data-pk")
  addArtworkToElement(pk, artworkElement, "sound-recording")


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
    addArtworkToElement(programPk, artworkElement, "radio")


watchYearSelect = ->
  $("#year-selector").on("change", (e) =>
    window.location = "?year=#{$(e.currentTarget).val()}"
  )


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
