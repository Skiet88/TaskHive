from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from helpers import apology
from service.TaskService import TaskService
from forms import TaskForm

#Create a routes manager for TaskController
task_bp = Blueprint("tasks", __name__)

#An object of TaskService to handle task-related database operations
task_service = TaskService()

# Dashboard route to display tasks and greeting
@task_bp.route("/")
@login_required  # Only logged-in users can access their dashboard
def dashboard():

    # Get query parameters for filtering tasks if any
    q = request.args.get("q")
    date = request.args.get("date")
    tasks = task_service.get_tasks_filtered(current_user.id, q, date)

    # Greeting based on the current time
    now = datetime.now()
    hour = now.hour
    if hour < 12:
        greeting = "Good Morning"
    elif hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    current_date = now.strftime("%A, %d %B %Y")

    form = TaskForm()

    # Render the dashboard page, passing in:
    # - the list of tasks
    # - the form object (for adding a new task)
    # - user info, greeting text, date, and filter values
    return render_template("dashboard.html",
                           tasks=tasks,
                           form=form,
                           user=current_user,
                           greeting=greeting,
                           current_date=current_date,
                           main_container_class="max-w-7xl",
                           q=q or "",
                           date=date or "")

# Add task route to handle form submission for creating a new task
@task_bp.route("/add-task", methods=["POST"])
@login_required
def add_task():
    # Create an add task form using flask WTForms Library
    form = TaskForm()

    if form.validate_on_submit(): #Ensure data validation on Submit
        title = form.title.data
        desc = form.description.data
        task_service.create_task(current_user.id, title, desc)
        flash("Task added successfully!!", "success")
        return redirect(url_for("tasks.dashboard"))
    else:
        flash("Please fill in all required fields", "error")
        return redirect(url_for("tasks.dashboard"))


# Route to delete a task
@task_bp.route("/delete-task/<int:task_id>")
@login_required
def delete_task(task_id):
    task_service.delete_task(task_id, current_user.id)
    flash("Task deleted successfully!!", "success")
    return redirect(url_for("tasks.dashboard"))

# Route to display the edit task form
@task_bp.route("/edit-task/<int:task_id>", methods=["GET"])
@login_required
def edit_task(task_id):
    tasks = task_service.get_tasks_filtered(current_user.id)
    # Find the task with the given ID
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        return apology("Task not found", 404)

    # Create an edit task form pre-populated with the task data
    form = TaskForm(obj=task)
    return render_template("EditTask.html",
                           form=form,
                           task=task,
                           main_container_class="max-w-xl")

# Route to handle the form submission for updating a task
@task_bp.route("/edit-task/<int:task_id>", methods=["POST"])
@login_required
def update_task(task_id):
    form = TaskForm()
    if form.validate_on_submit():
        title = form.title.data
        desc = form.description.data
        task_service.update_task(task_id, current_user.id, title, desc)
        flash("Task updated successfully !!", "success")
        return redirect(url_for("tasks.dashboard"))
    else:
        flash("Both fields required", "error")
        return redirect(url_for("tasks.edit_task", task_id=task_id))
