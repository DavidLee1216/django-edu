(function(e, t) {
	var n = function() {
		function r(t, r) {
			if (t == "dot") {
				r = '<ol class="dots">';
				e.each(n.li, function(e) {
					r += '<li class="' + (e == n.i ? t + " active" : t) + '">'
							+ ++e + "</li>"
				});
				r += "</ol>"
			} else {
				r = '<div class="';
				r = r + t + 's">' + r + t + ' prev">' + n.o.prev + "</div>" + r
						+ t + ' next">' + n.o.next + "</div></div>"
			}
			n.el.addClass("has-" + t + "s").append(r).find("." + t).click(
					function() {
						var t = e(this);
						t.hasClass("dot") ? n.stop().to(t.index()) : t
								.hasClass("prev") ? n.prev() : n.next()
					})
		}
		var n = this;
		n.o = {
			speed : 500,
			delay : 3e3,
			init : 0,
			pause : !t,
			loop : !t,
			keys : t,
			dots : t,
			arrows : t,
			prev : "&larr;",
			next : "&rarr;",
			fluid : t,
			starting : t,
			complete : t,
			items : ">ul",
			item : ">li",
			easing : "swing",
			autoplay : true
		};
		n.init = function(t, i) {
			n.o = e.extend(n.o, i);
			n.el = t;
			n.ul = t.find(n.o.items);
			n.max = [ t.outerWidth() | 0, t.outerHeight() | 0 ];
			n.li = n.ul.find(n.o.item).each(function(t) {
				var r = e(this), i = r.outerWidth(), s = r.outerHeight();
				if (i > n.max[0])
					n.max[0] = i;
				if (s > n.max[1])
					n.max[1] = s
			});
			var i = n.o, s = n.ul, o = n.li, u = o.length;
			n.i = 0;
			t.css({
				width : n.max[0],
				height : o.first().outerHeight(),
				overflow : "hidden"
			});
			s.css({
				position : "relative",
				left : 0,
				width : u * 100 + "%"
			});
			o.css({
				"float" : "left",
				width : n.max[0] + "px"
			});
			i.autoplay && setTimeout(function() {
				if (i.delay | 0) {
					n.play();
					if (i.pause) {
						t.on("mouseover mouseout", function(e) {
							n.stop();
							e.type == "mouseout" && n.play()
						})
					}
				}
			}, i.init | 0);
			if (i.keys) {
				e(document).keydown(function(e) {
					var t = e.which;
					if (t == 37)
						n.prev();
					else if (t == 39)
						n.next();
					else if (t == 27)
						n.stop()
				})
			}
			i.dots && r("dot");
			i.arrows && r("arrow");
			if (i.fluid) {
				e(window).resize(
						function() {
							n.r && clearTimeout(n.r);
							n.r = setTimeout(function() {
								var e = {
									height : o.eq(n.i).outerHeight()
								}, r = t.outerWidth();
								s.css(e);
								e["width"] = Math.min(Math.round(r
										/ t.parent().width() * 100), 100)
										+ "%";
								t.css(e)
							}, 50)
						}).resize()
			}
			if (e.event.special["swipe"] || e.Event("swipe")) {
				t.on("swipeleft swiperight swipeLeft swipeRight", function(e) {
					e.type.toLowerCase() == "swipeleft" ? n.next() : n.prev()
				})
			}
			return n
		};
		n.to = function(r, i) {
			if (n.t) {
				n.stop();
				n.play()
			}
			var s = n.o, o = n.el, u = n.ul, a = n.li, l = n.i, c = a.eq(r);
			e.isFunction(s.starting) && !i && s.starting(o, a.eq(l));
			if ((!c.length || r < 0) && s.loop == t)
				return;
			if (!c.length)
				r = 0;
			if (r < 0)
				r = a.length - 1;
			c = a.eq(r);
			var h = i ? 5 : s.speed | 0, p = s.easing, d = {
				height : c.outerHeight()
			};
			if (!u.queue("fx").length) {
				o.find(".dot").eq(r).addClass("active").siblings().removeClass(
						"active");
				o.animate(d, h, p) && u.animate(e.extend({
					left : "-" + r + "00%"
				}, d), h, p, function(t) {
					n.i = r;
					e.isFunction(s.complete) && !i && s.complete(o, c)
				})
			}
		};
		n.play = function() {
			n.t = setInterval(function() {
				n.to(n.i + 1)
			}, n.o.delay | 0)
		};
		n.stop = function() {
			n.t = clearInterval(n.t);
			return n
		};
		n.next = function() {
			return n.stop().to(n.i + 1)
		};
		n.prev = function() {
			return n.stop().to(n.i - 1)
		};
	};
	e.fn.unslider = function(t) {
		var r = this.length;
		return this
				.each(function(i) {
					var s = e(this), u = "unslider" + (r > 1 ? "-" + ++i : ""), a = (new n)
							.init(s, t);
					s.data(u, a).data("key", u)
				})
	};
	n.version = "1.0.0"
})(jQuery, false)
