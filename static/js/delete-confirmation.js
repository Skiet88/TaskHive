document.addEventListener("DOMContentLoaded", function () {
  const deleteForms = document.querySelectorAll("form.delete-task-form");

  deleteForms.forEach(form => {
    form.addEventListener("submit", function (e) {
      const confirmed = confirm("Are you sure you want to delete this task?");
      if (!confirmed) {
        e.preventDefault();
      }
    });
  });
});
