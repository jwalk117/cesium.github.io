document.addEventListener("DOMContentLoaded", () => {
  const menuButton = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".primary-nav");
  if (menuButton && nav) {
    menuButton.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      menuButton.setAttribute("aria-expanded", String(open));
    });
  }
  document.querySelectorAll(".dropdown-toggle").forEach(button => {
    button.addEventListener("click", () => {
      const parent = button.closest(".nav-dropdown");
      const open = parent.classList.toggle("open");
      button.setAttribute("aria-expanded", String(open));
    });
  });
  document.querySelectorAll("[data-year]").forEach(el => {
    el.textContent = new Date().getFullYear();
  });
});
