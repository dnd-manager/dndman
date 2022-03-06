from flask import Flask, render_template, request, redirect, url_for
import flask_login

import logging
import colorama

colorama.init()

from .logger import logger

logger.setLevel(logging.DEBUG)

from dotenv import load_dotenv
from os import getenv

from .blueprints import player, dm, auth, profile
from .database import database

from typing import Dict

load_dotenv()
app = Flask(__name__)

logger.info('Starting...')

auth.init_login_manager(app)

app.config.update(SECRET_KEY=getenv("SECRET_KEY"))

logger.info('Loading "Player" blueprint...')
app.register_blueprint(player.player, url_prefix="/player")

logger.info('Loading "DM" blueprint...')
app.register_blueprint(dm.dm, url_prefix="/dm")

logger.info('Loading "Auth" blueprint...')
app.register_blueprint(auth.auth, url_prefix="/auth")

logger.info('Loading "Profile" blueprint...')
app.register_blueprint(profile.profile, url_prefix="/profile")


@app.route("/protected")
def protected():
    return "Logged in as: " + flask_login.current_user.id

@app.route("/")
def home():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for("profile.profile_page"))
    return render_template("home.html")

logger.info('Started.')