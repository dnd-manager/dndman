from flask import Blueprint, render_template
import flask_login

dm = Blueprint("dm", __name__, static_folder="static", template_folder="templates")


@dm.route("/")
@flask_login.login_required
def dm_view():
    return render_template("dm/dm.html")


@dm.route("/map_editor")
@flask_login.login_required
def map_editor():
    return render_template("dm/map_editor.html")


@dm.route("/music_editor")
@flask_login.login_required
def music_editor():
    return render_template("dm/music_editor.html")


@dm.route("/campaign_preparer")
@flask_login.login_required
def campaign_preparer():
    return render_template("dm/campaign_preparer.html")
