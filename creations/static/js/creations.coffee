$(document).ready ->
  if $("body").attr("id") == "radio"
    initializeProgramInfoButtons()


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
