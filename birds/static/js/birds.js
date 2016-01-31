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
      var $elem, $window, bottom, height, top, viewport_bottom, viewport_height, viewport_top;
      $window = $(window);
      viewport_top = $window.scrollTop();
      viewport_height = $window.height();
      viewport_bottom = viewport_top + viewport_height;
      $elem = $(elem);
      top = $elem.offset().top;
      height = $elem.height();
      bottom = top + height;
      return top >= viewport_top && top < viewport_bottom || bottom > viewport_top && bottom <= viewport_bottom || height > viewport_height && top <= viewport_top && bottom >= viewport_bottom;
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
    classnames: {
      unloaded: "photo-and-caption--unloaded",
      loading: "photo-and-caption--loading",
      loaded: "photo-and-caption--loaded"
    },
    init: function() {
      var lazyScroll;
      lazyScroll = _.throttle(this.checkScroll.bind(this), 500);
      $(document).on("scroll", (function(_this) {
        return function(e) {
          return lazyScroll();
        };
      })(this));
      return this.checkScroll();
    },
    checkScroll: function() {
      return $(".photo-and-caption--unloaded:onScreen").each(function() {
        return PhotoChecklist.triggerLoad($(this));
      });
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
