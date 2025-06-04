from flask_wtf import FlaskForm # Base class for creating web forms with CSRF protection
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from service.UserService import UserService

# An object of UserService to handle user-related database operations
user_service = UserService()

class LoginForm(FlaskForm):
    """
      Form for user login: just email and password fields, with “required” checks.
    """
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In") # Button to submit the form

class RegisterForm(FlaskForm):
    """
      Form for user registration: email, name, surname, password and confirm password fields.
      It also checks that the email is not already registered.
    """
    email    = StringField("Email",
                           validators=[DataRequired(), Email(message="Enter a valid e-mail")])
    name     = StringField("First Name",
                           validators=[DataRequired(), Length(max=50)])
    surname  = StringField("Surname",
                           validators=[DataRequired(), Length(max=50)])
    password = PasswordField("Password",
                             validators=[DataRequired(), Length(min=6)])
    confirm  = PasswordField("Confirm",
                             validators=[DataRequired(),
                                         EqualTo("password", message="Passwords must match")])
    submit   = SubmitField("Register") # Button to submit the form

    # Validate that the email is not already registered
    def validate_email(self, field):
        if user_service.get_by_email(field.data):
            raise ValidationError("This e-mail is already registered")

class EditProfileForm(FlaskForm):
    """
      Form for editing user profile: name, surname, email fields.
      It checks that the email is not already registered by another user.
    """
    name = StringField("Name", validators=[DataRequired(), Length(max=50)])
    surname = StringField("Surname", validators=[DataRequired(), Length(max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Update Profile")

class ChangePwdForm(FlaskForm):
    """
      Form for changing user password: new password and confirm password fields.
      It checks that the new password matches the confirmation.
    """
    password = PasswordField("New Password", validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField("Confirm", validators=[
        DataRequired(),
        EqualTo("password", message="Passwords must match")
    ])
    submit = SubmitField("Update Password")

class TaskForm(FlaskForm):
    """
      Form for creating or editing tasks: title and description fields.
      It checks that both fields are filled in and have reasonable length limits.
    """
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    description = TextAreaField("Description", validators=[DataRequired(), Length(max=500)])
    submit = SubmitField("Save Task")
