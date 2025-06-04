from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from helpers import apology
from service.UserService import UserService
from service.AuthService import AuthService
from forms import LoginForm, ChangePwdForm

# Create a routes manager for AuthController (login, logout, change password)
auth_bp = Blueprint("auth", __name__)
auth_service = AuthService()
user_service = UserService()

# Registering the login route on the auth blueprint
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # Create a login form using flask WTForms Library
    form = LoginForm()

    #Check if user clicked “Submit” and data is valid
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Check the email/password against the database
        user = auth_service.authenticate_user(email, password)
        if not user:
            form.login_error = "Invalid email or password"
            return render_template("login.html", form=form)

        login_user(user)
        flash("Logged in successfully!", "success")
        return redirect(url_for("tasks.dashboard"))

    return render_template("login.html", form=form)



# Registering the change password route on the auth blueprint
@auth_bp.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    # Create a change password form using flask WTForms Library
    form = ChangePwdForm()
    if form.validate_on_submit():
        password = form.password.data
        confirm = form.confirm.data

        if password != confirm:
            return apology("Passwords do not match", 400)

        auth_service.change_password(current_user.id, password)
        flash("Password updated successfully!!", "success")
        return redirect(url_for("tasks.dashboard"))

    return render_template("change_password.html", form=form)


# Registering the logout route on the auth blueprint
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!!", "success")
    return redirect(url_for("auth.login"))
