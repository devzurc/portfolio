(function () {
  document.documentElement.classList.add("js-ready");

  const menu = document.getElementById("mobile-menu");
  const burger = document.getElementById("burgerBtn");
  const menuClose = document.getElementById("mobileMenuClose");
  const header = document.querySelector("[data-site-header]");
  const form = document.getElementById("contact-form");
  const feedback = document.getElementById("form-feedback");
  const sections = ["hero", "projects", "skills", "experience", "certifications", "job-fit", "contact"];
  const navLinks = document.querySelectorAll(".desktop-nav a, .mobile-menu-links a");
  let menuFocusTimeout;

  function isPortuguese() {
    return document.body.classList.contains("lang-pt");
  }

  function closeMenu(restoreFocus = true) {
    if (!menu || !burger) return;
    window.clearTimeout(menuFocusTimeout);
    menu.classList.remove("open");
    menu.setAttribute("aria-hidden", "true");
    burger.classList.remove("open");
    burger.setAttribute("aria-expanded", "false");
    if (restoreFocus) burger.focus();
  }

  function openMenu() {
    if (!menu || !burger) return;
    menu.classList.add("open");
    menu.setAttribute("aria-hidden", "false");
    burger.classList.add("open");
    burger.setAttribute("aria-expanded", "true");
    menuFocusTimeout = window.setTimeout(() => menuClose?.focus(), 100);
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
    document.querySelectorAll("[data-en][data-pt]").forEach((el) => {
      el.textContent = isPT ? el.dataset.pt : el.dataset.en;
    });
    document.querySelectorAll("[data-cv-en][data-cv-pt]").forEach((el) => {
      const href = isPT ? el.dataset.cvPt : el.dataset.cvEn;
      el.setAttribute("href", href);
      const file = href.split("?")[0].split("/").pop();
      if (el.hasAttribute("download")) el.setAttribute("download", file);
    });
    document.title = isPT
      ? "Lucas Cruz - Engenheiro de Dados Sênior & Automação com IA Generativa"
      : "Lucas Cruz - Senior Data Engineer & Gen. AI Automation Engineer";
    const description = document.querySelector('meta[name="description"]');
    if (description) {
      description.content = isPT ? description.dataset.metaDescPt : description.dataset.metaDescEn;
    }
    burger?.setAttribute("aria-label", isPT ? "Abrir menu" : "Open menu");
    document.querySelectorAll(".lang-toggle").forEach((toggle) => {
      toggle.setAttribute("aria-label", isPT ? "Seletor de idioma" : "Language selector");
    });
    try { localStorage.setItem("lc-lang", lang); } catch (_) { /* unavailable */ }
  }

  burger?.addEventListener("click", () => menu?.classList.contains("open") ? closeMenu() : openMenu());
  menuClose?.addEventListener("click", () => closeMenu());
  document.querySelectorAll("[data-menu-close]").forEach((link) => link.addEventListener("click", () => closeMenu(false)));
  document.querySelectorAll("[data-lang-button]").forEach((button) => {
    button.addEventListener("click", () => {
      setLang(button.dataset.langButton);
      if (menu?.classList.contains("open")) closeMenu(false);
    });
  });

  document.addEventListener("click", (event) => {
    if (menu?.classList.contains("open") && !menu.contains(event.target) && !burger?.contains(event.target)) closeMenu();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenu();
      document.querySelectorAll(".cv-dropdown[open]").forEach((el) => el.removeAttribute("open"));
    }
  });

  try { if (localStorage.getItem("lc-lang") === "pt") setLang("pt"); } catch (_) { /* unavailable */ }

  const revealObserver = "IntersectionObserver" in window
    ? new IntersectionObserver((entries) => entries.forEach((entry) => {
      if (entry.isIntersecting) { entry.target.classList.add("visible"); revealObserver.unobserve(entry.target); }
    }), { threshold: 0.08, rootMargin: "0px 0px -24px 0px" })
    : null;
  document.querySelectorAll(".fade-in").forEach((el, index) => {
    el.style.setProperty("--reveal-delay", `${Math.min(index % 4, 3) * 80}ms`);
    revealObserver ? revealObserver.observe(el) : el.classList.add("visible");
  });

  function setActiveNav(id) {
    navLinks.forEach((link) => link.classList.toggle("active", link.getAttribute("href") === `#${id}`));
  }
  setActiveNav("hero");
  if ("IntersectionObserver" in window) {
    const spy = new IntersectionObserver((entries) => entries.forEach((entry) => {
      if (entry.isIntersecting) setActiveNav(entry.target.id);
    }), { rootMargin: "-28% 0px -62% 0px", threshold: 0 });
    sections.forEach((id) => document.getElementById(id) && spy.observe(document.getElementById(id)));
  }
  window.addEventListener("scroll", () => header?.classList.toggle("is-scrolled", window.scrollY > 50), { passive: true });
  header?.classList.toggle("is-scrolled", window.scrollY > 50);

  if (form && feedback) {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const fields = ["name", "email", "subject", "message"].map((name) => form.elements.namedItem(name));
      const invalid = fields.find((field) => !field.value.trim() || (field.type === "email" && !field.validity.valid));
      fields.forEach((field) => field.setAttribute("aria-invalid", String(field === invalid)));
      if (invalid) {
        const invalidEmail = invalid.name === "email" && !invalid.validity.valid;
        feedback.textContent = invalidEmail
          ? (isPortuguese()
            ? "Informe um e-mail válido (por exemplo, nome@empresa.com)."
            : "Enter a valid email address (for example, name@company.com).")
          : (isPortuguese()
            ? "Preencha o campo destacado antes de continuar."
            : "Complete the highlighted field before continuing.");
        feedback.className = "form-feedback error";
        invalid.focus();
        return;
      }
      const data = new FormData(form);
      const name = data.get("name").trim();
      const email = data.get("email").trim();
      const subject = data.get("subject").trim();
      const message = data.get("message").trim();
      const body = isPortuguese()
        ? `Nome: ${name}\nE-mail: ${email}\n\n${message}`
        : `Name: ${name}\nEmail: ${email}\n\n${message}`;
      feedback.textContent = isPortuguese() ? "Abrindo seu cliente de e-mail com a mensagem preenchida." : "Opening your email client with the message prefilled.";
      feedback.className = "form-feedback success";
      window.location.href = `mailto:dev.lucascruz@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    });
    form.querySelectorAll("input,textarea").forEach((field) => field.addEventListener("input", () => field.setAttribute("aria-invalid", "false")));
  }
}());
