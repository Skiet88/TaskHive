document.addEventListener("DOMContentLoaded", () => {
  const flashMessages = document.querySelectorAll(".flash-message");
  flashMessages.forEach(msg => {
    setTimeout(() => {
      msg.classList.add("opacity-0", "transition-opacity", "duration-700");
      setTimeout(() => msg.remove(), 700);
    }, 3000);
  });
});
