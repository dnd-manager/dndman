from flask import Blueprint, render_template, request
import flask_login
import random

player = Blueprint(
    "player", __name__, static_folder="static", template_folder="templates"
)

rand_d: int = 0

@player.route("/")
@flask_login.login_required
def player_view():
    return render_template("player/player.html", rand_d=rand_d)

@player.route("/dice_roll", methods=["GET", "POST"])
@flask_login.login_required
def dice_roll():
    if request.method == "POST":
        dice_roll(request.form.get("range"))
    return render_template("player/player.html", rand_d=rand_d)

@player.route("/character_create/step1")
@flask_login.login_required
def character_creator():
    return render_template("player/character_creator/step1.html")

def dice_roll(max):
    global rand_d
    rand_d = random.randint(1, max)