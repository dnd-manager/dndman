from flask import Blueprint
from dndman import app

discord_compat = Blueprint("discord_compat", __name__, static_folder="static", template_folder="templates")

@discord_compat.route("/send_message/<msg>")
async def dc_compat(msg):
    await app.invoke_event_async("send_msg", msg)
    return ("", 200)