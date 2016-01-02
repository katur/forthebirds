$(document).ready ->
  if $("body").attr("id") == "birds"
    expandNoSubfamilies()
    createExpandButtons()


expandNoSubfamilies = ->
  $(".no-subfamily").next("ul").toggleClass("collapsed")


createExpandButtons = ->
  links = $(".plus-sign").closest("a")

  links.css("cursor", "pointer")

  links.click (e) ->
    e.preventDefault()
    $(this).toggleClass("active")
    $(this).find(".plus-sign").toggleClass("minus")
    $(this).closest("li").next("ul").toggleClass("collapsed")
