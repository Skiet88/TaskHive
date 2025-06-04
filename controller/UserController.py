from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user

from forms import RegisterForm, EditProfileForm
from service.UserService import UserService
from helpers import apology

#Create a routes manager for UserController
user_bp = Blueprint("user", __name__)

# An object of UserService to handle user-related database operations
user_service = UserService()

# Registering the user registration route on the user blueprint
@user_bp.route("/register", methods=["GET", "POST"])
def register():

    # Create a registration form using flask WTForms Library
    form = RegisterForm()
    if form.validate_on_submit(): # Ensure data validation on Submit

        user_service.create_user(
            form.name.data,
            form.surname.data,
            form.email.data,
            form.password.data
        )
        flash("Registration successful 🎉", "success")

        # Automatically log in the user after registration
        return redirect(url_for("auth.login"))

    # If the form is not valid, render the registration page with the form
    return render_template("register.html", form=form)


#Profile route to display user profile information
#This route is currently not in use/implemented in the UI
@user_bp.route("/profile/edit", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm(obj=current_user)

    if form.validate_on_submit():
        # Check if email is being changed to one that already exists
        existing = user_service.get_by_email(form.email.data)
        if existing and existing.id != current_user.id:
            return apology("E-mail already in use", 400)

        user_service.update_user(
            current_user.id,
            form.name.data,
            form.surname.data,
            form.email.data
        )

        # Keep session up to date
        current_user.name = form.name.data
        current_user.surname = form.surname.data
        current_user.email = form.email.data

        flash("Profile updated successfully 📝", "success")
        return redirect(url_for("user.profile"))

    # If the form is not valid, render the edit profile page with the form
    return render_template("edit_profile.html", form=form)


@user_bp.route("/profile/delete", methods=["POST"])
@login_required
def delete_account():
    user_service.delete_user(current_user.id)
    logout_user()
    flash("Account deleted permanently 🗑️", "success")
    return redirect(url_for("user.register"))
