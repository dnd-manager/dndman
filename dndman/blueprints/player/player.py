from flask import Blueprint, render_template
import flask_login

player = Blueprint(
    "player", __name__, static_folder="static", template_folder="templates"
)


@player.route("/")
@flask_login.login_required
def player_view():
    return render_template("player/player.html")


@player.route("/dice_roll")
@flask_login.login_required
def dice_roll():
    return render_template("player/dice_roll.html")


@player.route("/character_create/step1")
@flask_login.login_required
def character_creator():
    return render_template("player/character_creator/step1.html")
