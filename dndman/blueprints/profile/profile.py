from flask import Blueprint, render_template, redirect, url_for
import flask_login

profile = Blueprint(
    "profile", __name__, static_folder="static", template_folder="templates"
)

@profile.route("/")
def profile_page():
    return render_template("profile/profile.html", username=flask_login.current_user.id)
