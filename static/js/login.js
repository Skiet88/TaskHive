document.addEventListener("DOMContentLoaded", () => {
  const loginError = document.querySelector(".login-error");
  const emailInput = document.querySelector('input[name="email"]');
  const passwordInput = document.querySelector('input[name="password"]');

  if (loginError) {
    // Auto-hide after 10 seconds
    setTimeout(() => {
      loginError.classList.add("opacity-0", "transition-opacity", "duration-500");
      setTimeout(() => loginError.remove(), 500);
    }, 10000);

    // Remove error on typing
    [emailInput, passwordInput].forEach(input => {
      input.addEventListener("input", () => {
        loginError.remove();
      });
    });
  }
});
