(function () {
  document.documentElement.classList.add("js-ready");

  const menu = document.getElementById("mobile-menu");
  const burger = document.getElementById("burgerBtn");
  const sections = ["hero", "projects", "experience", "skills", "certifications", "job-fit", "contact"];

  function closeMenu() {
    if (!menu || !burger) return;
    menu.classList.remove("open");
    burger.classList.remove("open");
    burger.setAttribute("aria-expanded", "false");
    document.body.classList.remove("menu-open");
  }

  function toggleMenu() {
    if (!menu || !burger) return;
    const isOpen = menu.classList.contains("open");
    menu.classList.toggle("open", !isOpen);
    burger.classList.toggle("open", !isOpen);
    burger.setAttribute("aria-expanded", String(!isOpen));
    document.body.classList.toggle("menu-open", !isOpen);
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

    try {
      localStorage.setItem("lc-lang", lang);
    } catch (error) {
      /* Storage may be unavailable in strict browser settings. */
    }
  }

  if (burger) {
    burger.addEventListener("click", toggleMenu);
  }

  document.querySelectorAll("[data-menu-close]").forEach((link) => {
    link.addEventListener("click", closeMenu);
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

  /* ─── Active Scroll — Sidebar + Mobile Menu ─── */
  const sidebarLinks = document.querySelectorAll(".sidebar-nav a, .mobile-menu-links a");

  function updateActiveNav() {
    let current = "hero";

    sections.forEach((id) => {
      const el = document.getElementById(id);
      if (el && window.scrollY >= el.offsetTop - 160) current = id;
    });

    sidebarLinks.forEach((link) => {
      link.classList.toggle("active", link.getAttribute("href") === `#${current}`);
    });
  }

  /* Scope scroll listener to the main-content scrollable area or window */
  updateActiveNav();
  window.addEventListener("scroll", updateActiveNav, { passive: true });
})();
