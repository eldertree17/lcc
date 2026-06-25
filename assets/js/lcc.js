/* Lamma Cricket Club — site interactions */
(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    /* ---- highlight current page in nav ---- */
    var here = location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll(".nav a").forEach(function (a) {
      var href = (a.getAttribute("href") || "").split("/").pop();
      if (href && href === here) {
        a.classList.add("active");
        var wrap = a.closest(".wsite-menu-item-wrap");
        if (wrap) wrap.classList.add("active");
        var sub = a.closest(".wsite-menu-subitem-wrap");
        if (sub) sub.classList.add("wsite-nav-current");
      }
    });

    /* ---- mobile menu toggle ---- */
    var hamburger = document.querySelector(".hamburger");
    if (hamburger) {
      hamburger.addEventListener("click", function (e) {
        e.preventDefault();
        document.body.classList.toggle("nav-open");
      });
    }

    /* ---- build mobile menu by cloning desktop menu ---- */
    var desktopMenu = document.querySelector(".desktop-nav .wsite-menu-default");
    var mobileNav = document.querySelector(".mobile-nav");
    if (desktopMenu && mobileNav && !mobileNav.children.length) {
      mobileNav.appendChild(desktopMenu.cloneNode(true));
    }

    /* ---- mobile submenu expand/collapse ---- */
    if (mobileNav) {
      mobileNav.querySelectorAll("li").forEach(function (li) {
        var wrap = li.querySelector(":scope > .wsite-menu-wrap");
        var link = li.querySelector(":scope > a");
        if (wrap && link) {
          var arrow = document.createElement("span");
          arrow.className = "wsite-menu-arrow";
          arrow.textContent = "+";
          link.appendChild(arrow);
          link.addEventListener("click", function (e) {
            e.preventDefault();
            li.classList.toggle("open");
            arrow.textContent = li.classList.contains("open") ? "–" : "+";
          });
        }
      });
    }

    /* ---- constitution scrollspy ---- */
    var navLinks = Array.prototype.slice.call(
      document.querySelectorAll(".const-nav a[href^='#']")
    );
    if (navLinks.length) {
      var sections = navLinks
        .map(function (a) {
          var el = document.getElementById(a.getAttribute("href").slice(1));
          return el ? { link: a, el: el } : null;
        })
        .filter(Boolean);

      var setActive = function () {
        var pos = window.scrollY + 120;
        var current = sections[0];
        for (var i = 0; i < sections.length; i++) {
          if (sections[i].el.offsetTop <= pos) current = sections[i];
        }
        navLinks.forEach(function (a) { a.classList.remove("active"); });
        if (current) {
          current.link.classList.add("active");
          current.link.scrollIntoView({ block: "nearest" });
        }
      };

      var ticking = false;
      window.addEventListener("scroll", function () {
        if (!ticking) {
          window.requestAnimationFrame(function () {
            setActive();
            ticking = false;
          });
          ticking = true;
        }
      });
      setActive();
    }
  });
})();
