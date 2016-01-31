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


# onScreen jQuery plugin v0.2.1
# (c) 2011-2013 Ben Pickles
#
# http://benpickles.github.io/onScreen
#
# Released under MIT license.
#
# Modified by Michael P. Geraci to use getBoundingClientRect, optionally have a
# buffer, and cache window size. Depends on PhotoChecklist for caching instead
# of globals.
(($) ->
  $.expr[':'].onScreen = (elem) ->
    $window = $(window)

    if !PhotoChecklist.windowHeight
      PhotoChecklist.windowHeight = $window.height()

    buffer = PhotoChecklist.buffer || 0
    windowTop = $window.scrollTop()
    windowBottom = windowTop + PhotoChecklist.windowHeight
    rect = elem.getBoundingClientRect()
    top = rect.top + windowTop
    bottom = rect.bottom + windowTop

    topIsVisible = top >= (windowTop - buffer) && top < (windowBottom + buffer)
    bottomIsVisible = bottom > (windowTop - buffer) && bottom <= (windowBottom + buffer)
    isBiggerThanScreen = rect.height? && rect.height > PhotoChecklist.windowHeight && top <= (windowTop - buffer) && bottom >= (windowBottom + buffer)

    return topIsVisible || bottomIsVisible || isBiggerThanScreen

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
  # how close an elements needs to be to the viewport to trigger load
  buffer: 300

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

    lazyResize = _.throttle(@checkResize.bind(@), 500)
    $(window).on("resize", (e) =>
      lazyResize()
    )

    # load the first set before scroll
    @checkScroll()

  checkScroll: ->
    # scoping in here is a little whack: because we want to use `this` for
		# the jQuery each loop, refer to the singleton for triggerLoad
    $(".photo-and-caption--unloaded:onScreen").each( ->
      PhotoChecklist.triggerLoad($(@))
    )

  checkResize: ->
    @windowHeight = $(window).height()

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
