from flask import Blueprint, render_template, redirect, url_for
from dndman.database.database import User

import flask_login

profile = Blueprint(
    "profile", __name__, static_folder="static", template_folder="templates"
)


@profile.route("/")
@flask_login.login_required
def profile_page():
    return render_template(
        "profile/profile.html",
        username=flask_login.current_user.username,
        pfp=flask_login.current_user.pfp_path,
    )
