(function() {
  var _, createExpandButtons, expandNoSubfamilies;

  $(document).ready(function() {
    var page;
    page = $("body").attr("id");
    if (page === "birds") {
      expandNoSubfamilies();
      createExpandButtons();
    }
    if (page === "photo-checklist") {
      return PhotoChecklist.init();
    }
  });

  expandNoSubfamilies = function() {
    return $(".no-subfamily").next("ul").toggleClass("collapsed");
  };

  createExpandButtons = function() {
    var links;
    links = $(".plus-sign").closest("a");
    links.css("cursor", "pointer");
    return links.click(function(e) {
      e.preventDefault();
      $(this).toggleClass("active");
      $(this).find(".plus-sign").toggleClass("minus");
      return $(this).closest("li").next("ul").toggleClass("collapsed");
    });
  };

  (function($) {
    $.expr[':'].onScreen = function(elem) {
      var $window, bottom, bottomIsVisible, buffer, isBiggerThanScreen, rect, top, topIsVisible, windowBottom, windowTop;
      $window = $(window);
      if (!PhotoChecklist.windowHeight) {
        PhotoChecklist.windowHeight = $window.height();
      }
      buffer = PhotoChecklist.buffer || 0;
      windowTop = $window.scrollTop();
      windowBottom = windowTop + PhotoChecklist.windowHeight;
      rect = elem.getBoundingClientRect();
      top = rect.top + windowTop;
      bottom = rect.bottom + windowTop;
      topIsVisible = top >= (windowTop - buffer) && top < (windowBottom + buffer);
      bottomIsVisible = bottom > (windowTop - buffer) && bottom <= (windowBottom + buffer);
      isBiggerThanScreen = (rect.height != null) && rect.height > PhotoChecklist.windowHeight && top <= (windowTop - buffer) && bottom >= (windowBottom + buffer);
      return topIsVisible || bottomIsVisible || isBiggerThanScreen;
    };
  })(jQuery);

  _ = {};

  _.now = Date.now || function() {
    return (new Date).getTime();
  };

  _.throttle = function(func, wait, options) {
    var args, context, later, previous, result, timeout;
    context = void 0;
    args = void 0;
    result = void 0;
    timeout = null;
    previous = 0;
    if (!options) {
      options = {};
    }
    later = function() {
      previous = options.leading === false ? 0 : _.now();
      timeout = null;
      result = func.apply(context, args);
      if (!timeout) {
        context = args = null;
      }
    };
    return function() {
      var now, remaining;
      now = _.now();
      if (!previous && options.leading === false) {
        previous = now;
      }
      remaining = wait - (now - previous);
      context = this;
      args = arguments;
      if (remaining <= 0 || remaining > wait) {
        if (timeout) {
          clearTimeout(timeout);
          timeout = null;
        }
        previous = now;
        result = func.apply(context, args);
        if (!timeout) {
          context = args = null;
        }
      } else if (!timeout && options.trailing !== false) {
        timeout = setTimeout(later, remaining);
      }
      return result;
    };
  };

  window.PhotoChecklist = {
    buffer: 300,
    classnames: {
      unloaded: "photo-and-caption--unloaded",
      loading: "photo-and-caption--loading",
      loaded: "photo-and-caption--loaded"
    },
    init: function() {
      var lazyResize, lazyScroll;
      lazyScroll = _.throttle(this.checkScroll.bind(this), 500);
      $(document).on("scroll", (function(_this) {
        return function(e) {
          return lazyScroll();
        };
      })(this));
      lazyResize = _.throttle(this.checkResize.bind(this), 500);
      $(window).on("resize", (function(_this) {
        return function(e) {
          return lazyResize();
        };
      })(this));
      return this.checkScroll();
    },
    checkScroll: function() {
      return $(".photo-and-caption--unloaded:onScreen").each(function() {
        return PhotoChecklist.triggerLoad($(this));
      });
    },
    checkResize: function() {
      return this.windowHeight = $(window).height();
    },
    triggerLoad: function(el) {
      var img;
      if (el.hasClass(this.classnames.loaded)) {
        return;
      }
      if (el.hasClass(this.classnames.loading)) {
        return;
      }
      el.removeClass(this.classnames.unloaded).addClass(this.classnames.loading);
      img = new Image();
      return $(img).on("load", (function(_this) {
        return function() {
          return el.removeClass(_this.classnames.loading).prepend(img);
        };
      })(this)).attr("src", el.attr("data-src"));
    }
  };

}).call(this);
