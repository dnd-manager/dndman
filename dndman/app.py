from threading import Thread
from typing import Any, Callable, Iterable, Mapping
from flask import Flask, render_template, redirect, url_for
from dndman.utils.event import Event

import flask_login
import logging
import colorama

colorama.init()
from .logger import logger
logger.setLevel(logging.DEBUG)

from dotenv import load_dotenv
from os import getenv

from .blueprints import player, dm, auth, profile, discord_compat

class DnDManFlask(Flask):
    def create_event(self, event: Event):
        self.event = event

    def add_event_listener(self, event_id: str, listener):
        self.event.add_listener(event_id, listener)

    def invoke_event(self, event_id: str, *argv):
        self.event.invoke(event_id, argv)

    async def invoke_event_async(self, event_id: str, *argv):
        await self.event.invoke_async(event_id, argv)

logger.info("Starting...")

load_dotenv()
app = DnDManFlask(__name__)
app.config.update(SECRET_KEY=getenv("SECRET_KEY"))
auth.init_login_manager(app)


logger.info('Loading "Player" blueprint...')
app.register_blueprint(player.player, url_prefix="/player")

logger.info('Loading "DM" blueprint...')
app.register_blueprint(dm.dm, url_prefix="/dm")

logger.info('Loading "Auth" blueprint...')
app.register_blueprint(auth.auth, url_prefix="/auth")

logger.info('Loading "Profile" blueprint...')
app.register_blueprint(profile.profile, url_prefix="/profile")

logger.info('Loading "Discord Compatibility" blueprint...')
app.register_blueprint(discord_compat.discord_compat, url_prefix="/discord_compat")


@app.route("/")
def home():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for("profile.profile_page"))
    return render_template("home.html")

logger.info("Started.")


class FlaskWebThread(Thread):
    def __init__(self, group: None = None, target: Callable[..., Any] | None = ..., name: str | None = ..., args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = ..., *, daemon: bool | None = ..., comm_event: Event) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.comm_event = comm_event

    def run(self):
        app.create_event(self.comm_event)
        app.run("localhost", 8000)
        return super().run()