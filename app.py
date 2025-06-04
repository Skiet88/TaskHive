from flask import Flask # Main Flask application instance
from flask_login import LoginManager # Manages user session and authentication
from flask_wtf import CSRFProtect # Enables CSRF protection on all forms

# Importing configuration settings
from config import Config

# Importing blueprints for different controllers
from controller.AuthController import auth_bp
from controller.TaskController import task_bp
from controller.UserController import user_bp
from service.UserService import UserService

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)
CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"  # Redirect here when @login_required fails

user_service = UserService()

"""
    Given a user_id (stored in session), return the corresponding User object.
    Flask-Login uses this to load current_user.
"""
@login_manager.user_loader
def load_user(user_id):
    return user_service.get_by_id(user_id)

#Bluepeint registrations which wire up the URLs.
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)
app.register_blueprint(user_bp)

#Ensures that the browser doesn't cache any pages,but always fetch fresh ones each time.
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


if __name__ == "__main__":
    app.run(debug=True)
