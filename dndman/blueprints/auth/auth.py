from flask import Blueprint, render_template, request, redirect, url_for, flash
import flask_login

from dndman.database import database, User, UserNotFoundException

auth = Blueprint("auth", __name__, static_folder="static", template_folder="templates")

login_manager = flask_login.LoginManager()


def init_login_manager(app):
    login_manager.init_app(app)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth.login"))


@login_manager.user_loader
def user_loader(username):
    if not database.has_user(username):
        return

    user = User()
    user.id = username
    return user


@login_manager.request_loader
def request_loader(request):
    username = request.form.get("username")
    if not database.has_user(username):
        return

    user = User()
    user.id = username
    return user


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")

    return login_internal(request.form["username"], request.form["password"])


def login_internal(username, password):
    print(username + " requested a login")

    try:
        user = database.get_user(username)
        if user.password == password:
            flask_login.login_user(user)
            loggedIn = True
            return redirect(url_for("profile.profile_page"))
        else:
            flash("Password is incorrect", "error")
            pass
    except UserNotFoundException:
        flash("User name not found", "error")
    else:
        flash("Bad login, try again", "error")

    return redirect(url_for("auth.login"))


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("auth/signup.html")

    return signup_internal(
        request.form["username"],
        request.form["password"],
        request.form["password-confirmation"],
    )


def signup_internal(username, password, password_confirmation):
    print(username + " requested a signup")

    # if signup uses a user name already exist we do not proceed
    if database.has_user(username):
        flash("User with this name already exists!")
        return redirect(url_for("auth.signup"))

    # if password confirmation is different than password we do not proceed
    if password != password_confirmation:
        flash("The second password is not the same as the first one!")
        return redirect(url_for("auth.signup"))

    # create user
    user = User()
    user.id = username
    user.password = password
    database.add_user(user)

    login_internal(username, password)

    return redirect(url_for("auth.login"))


@auth.route("/logout")
def logout():
    flask_login.logout_user()
    return redirect(url_for("auth.login"))
