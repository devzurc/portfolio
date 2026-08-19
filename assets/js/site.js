(function () {
  document.documentElement.classList.add("js-ready");

  const menu = document.getElementById("mobile-menu");
  const burger = document.getElementById("burgerBtn");
  const menuClose = document.getElementById("mobileMenuClose");
  const mainContent = document.querySelector(".main-content");
  const sections = ["hero", "projects", "experience", "skills", "certifications", "job-fit", "contact"];
  let menuFocusTimeout;

  function closeMenu(restoreFocus = true) {
    if (!menu || !burger) return;
    window.clearTimeout(menuFocusTimeout);
    menu.classList.remove("open");
    menu.setAttribute("aria-hidden", "true");
    burger.classList.remove("open");
    burger.setAttribute("aria-expanded", "false");
    document.body.classList.remove("menu-open");
    if (mainContent) mainContent.removeAttribute("inert");
    if (restoreFocus) burger.focus();
  }

  function openMenu() {
    if (!menu || !burger) return;
    menu.classList.add("open");
    menu.setAttribute("aria-hidden", "false");
    burger.classList.add("open");
    burger.setAttribute("aria-expanded", "true");
    document.body.classList.add("menu-open");
    if (mainContent) mainContent.setAttribute("inert", "");
    menuFocusTimeout = window.setTimeout(() => menuClose?.focus(), 150);
  }

  function toggleMenu() {
    if (menu?.classList.contains("open")) {
      closeMenu();
    } else {
      openMenu();
    }
  }

  function setLang(lang) {
    const isPT = lang === "pt";
    document.body.classList.toggle("lang-pt", isPT);
    document.documentElement.lang = isPT ? "pt-BR" : "en";
    document.documentElement.dataset.lang = isPT ? "pt-BR" : "en";

    document.querySelectorAll("[data-lang-button]").forEach((button) => {
      const active = button.dataset.langButton === lang;
      button.classList.toggle("active", active);
      button.setAttribute("aria-pressed", String(active));
    });

    document.title = isPT
      ? "Lucas Cruz - Engenheiro de Dados Sênior & Automação com IA Generativa"
      : "Lucas Cruz - Senior Data Engineer & Gen. AI Automation Engineer";

    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) {
      const enDesc = metaDesc.dataset.metaDescEn || metaDesc.content;
      const ptDesc = metaDesc.dataset.metaDescPt || metaDesc.content;
      metaDesc.setAttribute("content", isPT ? ptDesc : enDesc);
    }

    document.querySelectorAll("[data-en][data-pt]").forEach((el) => {
      el.textContent = isPT ? el.dataset.pt : el.dataset.en;
    });

    burger?.setAttribute("aria-label", isPT ? "Abrir menu" : "Open menu");
    document.querySelectorAll(".lang-toggle").forEach((toggle) => {
      toggle.setAttribute("aria-label", isPT ? "Seletor de idioma" : "Language selector");
    });

    try {
      localStorage.setItem("lc-lang", lang);
    } catch (error) {
      /* Storage may be unavailable in strict browser settings. */
    }
  }

  if (burger) {
    burger.addEventListener("click", toggleMenu);
  }
  menuClose?.addEventListener("click", () => closeMenu());

  document.querySelectorAll("[data-menu-close]").forEach((link) => {
    link.addEventListener("click", () => closeMenu(false));
  });

  document.querySelectorAll("[data-lang-button]").forEach((button) => {
    button.addEventListener("click", () => {
      setLang(button.dataset.langButton);
      closeMenu();
    });
  });

  document.addEventListener("click", (event) => {
    if (!menu || !burger) return;
    if (menu.classList.contains("open") && !menu.contains(event.target) && !burger.contains(event.target)) {
      closeMenu();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenu();
      document.querySelectorAll(".cv-dropdown[open]").forEach((el) => el.removeAttribute("open"));
    }
    if (event.key === "Tab" && menu?.classList.contains("open")) {
      const focusable = [...menu.querySelectorAll('a[href], button:not([disabled]), summary, [tabindex]:not([tabindex="-1"])')]
        .filter((el) => !el.closest("[aria-hidden='true']") && el.getClientRects().length > 0);
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (!first || !last) return;
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
  });

  (function restoreLanguage() {
    try {
      const saved = localStorage.getItem("lc-lang");
      if (saved === "pt") setLang("pt");
    } catch (error) {
      /* Storage may be unavailable in strict browser settings. */
    }
  })();

  /* ─── Scroll Intersection Reveals ─── */
  const observer = "IntersectionObserver" in window
    ? new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          window.setTimeout(() => entry.target.classList.add("visible"), Number(entry.target.dataset.delay || 0));
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.05, rootMargin: "0px 0px -40px 0px" })
    : null;

  document.querySelectorAll(".fade-in, .job, .skill-card, .cert-card, .badge-card, .fit-card, .contact-link-item, .work-item, .profile-card").forEach((el, index) => {
    el.dataset.delay = String((index % 5) * 60);
    if (observer) {
      observer.observe(el);
    } else {
      el.classList.add("visible");
    }
  });

  /* ─── Active section — Sidebar + Mobile Menu ─── */
  const sidebarLinks = document.querySelectorAll(".sidebar-nav a, .mobile-menu-links a");

  function setActiveNav(current) {
    sidebarLinks.forEach((link) => {
      link.classList.toggle("active", link.getAttribute("href") === `#${current}`);
    });
  }

  setActiveNav("hero");
  if ("IntersectionObserver" in window) {
    const navObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) setActiveNav(entry.target.id);
      });
    }, { rootMargin: "-20% 0px -65% 0px", threshold: 0 });
    sections.forEach((id) => {
      const section = document.getElementById(id);
      if (section) navObserver.observe(section);
    });
  }
})();
