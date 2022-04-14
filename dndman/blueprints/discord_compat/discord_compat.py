from flask import Blueprint

discord_compat = Blueprint("discord_compat", __name__, static_folder="static", template_folder="templates")

@discord_compat.route("/send_message/<msg>")
async def dc_compat(msg):
    print('hallo 1')
    return ("", 200)