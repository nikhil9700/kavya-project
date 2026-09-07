(() => {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const coarsePointer = window.matchMedia("(hover: none), (pointer: coarse)").matches;
  const body = document.body;
  const html = document.documentElement;

  if (coarsePointer) body.classList.add("has-coarse-pointer");

  /* Theme */
  const themeToggle = document.querySelector("[data-theme-toggle]");
  const storedTheme = localStorage.getItem("kavya-theme");
  const preferredLight = window.matchMedia("(prefers-color-scheme: light)").matches;
  const initialTheme = storedTheme || (preferredLight ? "light" : "dark");
  html.setAttribute("data-theme", initialTheme);

  const setTheme = (theme) => {
    html.setAttribute("data-theme", theme);
    localStorage.setItem("kavya-theme", theme);
    document.querySelector('meta[name="theme-color"]')?.setAttribute(
      "content",
      theme === "dark" ? "#070b12" : "#eef3f8"
    );
  };

  themeToggle?.addEventListener("click", () => {
    const next = html.getAttribute("data-theme") === "dark" ? "light" : "dark";
    setTheme(next);
  });

  /* Year */
  document.querySelectorAll("[data-year]").forEach((el) => {
    el.textContent = String(new Date().getFullYear());
  });

  /* Header / nav */
  const header = document.querySelector("[data-header]");
  const toggle = document.querySelector("[data-nav-toggle]");
  const nav = document.querySelector("[data-nav]");

  const setScrolled = () => {
    if (!header) return;
    const y = window.scrollY || document.documentElement.scrollTop || 0;
    // Solid nav while content scrolls underneath; clear only at very top
    if (y <= 8) {
      header.classList.remove("is-scrolled");
    } else {
      header.classList.add("is-scrolled");
    }
  };
  setScrolled();
  window.addEventListener("scroll", setScrolled, { passive: true });
  window.addEventListener("resize", setScrolled, { passive: true });

  const closeNav = () => {
    header?.classList.remove("is-open");
    toggle?.setAttribute("aria-expanded", "false");
  };

  toggle?.addEventListener("click", () => {
    const open = header?.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });

  nav?.querySelectorAll("a").forEach((link) => link.addEventListener("click", closeNav));
  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeNav();
  });

  /* Custom cursor */
  const cursorDot = document.querySelector(".cursor-dot");
  const cursorRing = document.querySelector(".cursor-ring");
  let mouseX = -100;
  let mouseY = -100;
  let ringX = -100;
  let ringY = -100;
  let cursorVisible = false;

  if (!coarsePointer && cursorDot && cursorRing && !reduceMotion) {
    const showCursor = (x, y) => {
      mouseX = x;
      mouseY = y;
      cursorDot.style.transform = `translate(${x}px, ${y}px) translate(-50%, -50%)`;
      if (!cursorVisible) {
        cursorVisible = true;
        body.classList.add("cursor-active");
      }
    };

    const hideCursor = () => {
      cursorVisible = false;
      body.classList.remove("cursor-active", "cursor-hover", "cursor-click");
    };

    window.addEventListener(
      "mousemove",
      (e) => {
        // Ignore edge glitches Chrome fires while scrolling / leaving the window
        if (
          e.clientY < 12 ||
          e.clientX < 2 ||
          e.clientY >= window.innerHeight - 2 ||
          e.clientX >= window.innerWidth - 2
        ) {
          hideCursor();
          return;
        }
        showCursor(e.clientX, e.clientY);
      },
      { passive: true }
    );

    document.addEventListener("mouseleave", hideCursor);
    window.addEventListener("blur", hideCursor);

    const tickCursor = () => {
      if (cursorVisible) {
        ringX += (mouseX - ringX) * 0.18;
        ringY += (mouseY - ringY) * 0.18;
        cursorRing.style.transform = `translate(${ringX}px, ${ringY}px) translate(-50%, -50%)`;
      }
      requestAnimationFrame(tickCursor);
    };
    tickCursor();

    document.addEventListener("mousedown", () => {
      if (cursorVisible) body.classList.add("cursor-click");
    });
    document.addEventListener("mouseup", () => body.classList.remove("cursor-click"));

    const hoverTargets = "a, button, [data-magnetic], .project-row, .contact-item, .theme-toggle";
    document.querySelectorAll(hoverTargets).forEach((el) => {
      el.addEventListener("mouseenter", () => {
        if (cursorVisible) body.classList.add("cursor-hover");
      });
      el.addEventListener("mouseleave", () => body.classList.remove("cursor-hover"));
    });
  }

  /* Magnetic buttons */
  if (!coarsePointer && !reduceMotion) {
    document.querySelectorAll("[data-magnetic]").forEach((el) => {
      el.addEventListener("mousemove", (e) => {
        const rect = el.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        el.style.transform = `translate(${x * 0.18}px, ${y * 0.22}px)`;
      });
      el.addEventListener("mouseleave", () => {
        el.style.transform = "";
      });
    });
  }

  /* Ambient orbs canvas */
  const canvas = document.getElementById("orb-canvas");
  if (canvas && !reduceMotion) {
    const ctx = canvas.getContext("2d");
    let width = 0;
    let height = 0;
    let orbs = [];
    let pointer = { x: 0.5, y: 0.5 };

    const resize = () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
      orbs = Array.from({ length: Math.min(7, Math.floor(width / 220)) }, (_, i) => ({
        x: Math.random() * width,
        y: Math.random() * height,
        r: 80 + Math.random() * 160,
        vx: (Math.random() - 0.5) * 0.25,
        vy: (Math.random() - 0.5) * 0.25,
        hue: i % 2 === 0 ? 168 : 198,
      }));
    };

    window.addEventListener("resize", resize);
    window.addEventListener(
      "pointermove",
      (e) => {
        pointer.x = e.clientX / width;
        pointer.y = e.clientY / height;
      },
      { passive: true }
    );
    resize();

    const draw = () => {
      ctx.clearRect(0, 0, width, height);
      const dark = html.getAttribute("data-theme") !== "light";
      orbs.forEach((orb) => {
        orb.x += orb.vx + (pointer.x - 0.5) * 0.35;
        orb.y += orb.vy + (pointer.y - 0.5) * 0.25;
        if (orb.x < -orb.r) orb.x = width + orb.r;
        if (orb.x > width + orb.r) orb.x = -orb.r;
        if (orb.y < -orb.r) orb.y = height + orb.r;
        if (orb.y > height + orb.r) orb.y = -orb.r;

        const gradient = ctx.createRadialGradient(orb.x, orb.y, 0, orb.x, orb.y, orb.r);
        gradient.addColorStop(0, `hsla(${orb.hue}, 70%, ${dark ? 55 : 40}%, ${dark ? 0.16 : 0.1})`);
        gradient.addColorStop(1, "transparent");
        ctx.fillStyle = gradient;
        ctx.beginPath();
        ctx.arc(orb.x, orb.y, orb.r, 0, Math.PI * 2);
        ctx.fill();
      });
      requestAnimationFrame(draw);
    };
    draw();
  }

  /* Loader + GSAP */
  const loader = document.querySelector("[data-loader]");
  const loaderBar = loader?.querySelector(".loader-bar span");

  const finishLoader = () => {
    if (loader) {
      loader.classList.add("is-done");
      loader.style.display = "none";
      loader.remove();
    }
    body.classList.add("is-loaded");
  };

  // Safety: never leave visitors stuck on the intro screen
  window.setTimeout(() => {
    if (!body.classList.contains("is-loaded")) finishLoader();
  }, 2200);

  // Also dismiss if the tab was background-throttled
  document.addEventListener("visibilitychange", () => {
    if (!document.hidden && !body.classList.contains("is-loaded")) finishLoader();
  });

  const initReveals = () => {
    document.querySelectorAll("[data-reveal]").forEach((el) => el.classList.add("is-visible"));

    if (typeof gsap === "undefined" || reduceMotion) return;

    gsap.registerPlugin(ScrollTrigger);

    // Homepage only: animate reveals; project pages stay visible via CSS
    if (body.classList.contains("page-project")) return;

    document.querySelectorAll("[data-reveal]").forEach((el) => {
      gsap.fromTo(
        el,
        { y: 28, opacity: 0.15 },
        {
          y: 0,
          opacity: 1,
          duration: 0.8,
          ease: "power3.out",
          scrollTrigger: {
            trigger: el,
            start: "top 90%",
            toggleActions: "play none none none",
          },
        }
      );
    });

    document.querySelectorAll("[data-tilt]").forEach((panel) => {
      if (coarsePointer) return;
      panel.addEventListener("mousemove", (e) => {
        const rect = panel.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        panel.style.transform = `perspective(900px) rotateY(${x * 6}deg) rotateX(${-y * 6}deg) translateY(-4px)`;
      });
      panel.addEventListener("mouseleave", () => {
        panel.style.transform = "";
      });
    });
  };

  const runIntro = () => {
    initReveals();

    if (!loader) {
      finishLoader();
      return;
    }

    if (typeof gsap === "undefined") {
      finishLoader();
      return;
    }

    gsap.registerPlugin(ScrollTrigger);

    const tl = gsap.timeline({
      onComplete: () => {
        finishLoader();
      },
    });

    tl.to({}, { duration: 1.35 });
    tl.add(() => finishLoader());

    const heroLines = document.querySelectorAll("[data-hero-line]");
    const heroImg = document.querySelector("[data-hero-img]");

    if (heroImg) {
      gsap.set(heroImg, { clearProps: "transform,translate,rotate,scale,transformOrigin" });
    }

    if (heroLines.length && !reduceMotion) {
      gsap.set(heroLines, { y: 36, opacity: 0 });
      tl.to(
        heroLines,
        {
          y: 0,
          opacity: 1,
          duration: 0.9,
          stagger: 0.08,
          ease: "power3.out",
        },
        0.2
      );
    } else {
      heroLines.forEach((el) => {
        el.style.opacity = "1";
        el.style.transform = "none";
      });
    }
  };

  if (reduceMotion) {
    finishLoader();
    document.querySelectorAll("[data-reveal], [data-hero-line]").forEach((el) => {
      el.classList.add("is-visible");
      el.style.opacity = "1";
      el.style.transform = "none";
    });
  } else if (document.readyState === "complete") {
    runIntro();
  } else {
    window.addEventListener("load", runIntro, { once: true });
  }
})();
