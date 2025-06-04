document.addEventListener("DOMContentLoaded", () => {
  const inputs = document.querySelectorAll("input");

  inputs.forEach(input => {
    input.addEventListener("input", () => {
      const error = input.parentElement.querySelector("p.text-red-500");
      if (error) {
        error.remove();
        input.classList.remove("border-red-500");
        input.classList.add("border-gray-600");
      }
    });
  });
});
