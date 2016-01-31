$(document).ready ->
  page = $("body").attr("id")

  if page == "birds"
    expandNoSubfamilies()
    createExpandButtons()

  if page == "photo-checklist"
    PhotoChecklist.init()


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


# TODO rewrite this fucker to use getBoundingClientRect()
# onScreen jQuery plugin v0.2.1
# (c) 2011-2013 Ben Pickles
#
# http://benpickles.github.io/onScreen
#
# Released under MIT license.
(($) ->

  $.expr[':'].onScreen = (elem) ->
    $window = $(window)
    viewport_top = $window.scrollTop()
    viewport_height = $window.height()
    viewport_bottom = viewport_top + viewport_height
    $elem = $(elem)
    top = $elem.offset().top
    height = $elem.height()
    bottom = top + height

    return top >= viewport_top and top < viewport_bottom or
      bottom > viewport_top and bottom <= viewport_bottom or
      height > viewport_height and top <= viewport_top and bottom >= viewport_bottom

  return
) jQuery


# now and throttle taken from underscore.js
_ = {}
_.now = Date.now or ->
  (new Date).getTime()

_.throttle = (func, wait, options) ->
  context = undefined
  args = undefined
  result = undefined
  timeout = null
  previous = 0
  if !options
    options = {}

  later = ->
    previous = if options.leading == false then 0 else _.now()
    timeout = null
    result = func.apply(context, args)
    if !timeout
      context = args = null
    return

  ->
    now = _.now()
    if !previous and options.leading == false
      previous = now
    remaining = wait - (now - previous)
    context = this
    args = arguments
    if remaining <= 0 or remaining > wait
      if timeout
        clearTimeout timeout
        timeout = null
      previous = now
      result = func.apply(context, args)
      if !timeout
        context = args = null
    else if !timeout and options.trailing != false
      timeout = setTimeout(later, remaining)
    result


window.PhotoChecklist = {
  classnames: {
    unloaded: "photo-and-caption--unloaded"
    loading: "photo-and-caption--loading"
    loaded: "photo-and-caption--loaded"
  }

  init: ->
    lazyScroll = _.throttle(@checkScroll.bind(@), 500)
    $(document).on("scroll", (e) =>
      lazyScroll()
    )

    # load the first set before scroll
    @checkScroll()

  checkScroll: ->
    # scoping in here is a little whack: because we want to use `this` for
		# the jQuery each loop, refer to the singleton for triggerLoad
    $(".photo-and-caption--unloaded:onScreen").each( ->
      PhotoChecklist.triggerLoad($(@))
    )

  triggerLoad: (el) ->
    return if el.hasClass(@classnames.loaded)
    return if el.hasClass(@classnames.loading)

    el
      .removeClass(@classnames.unloaded)
      .addClass(@classnames.loading)

    img = new Image()

    $(img).on("load", =>
      el
        .removeClass(@classnames.loading)
        .prepend(img)
    ).attr("src", el.attr("data-src"))
}
