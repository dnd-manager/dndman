from flask import Blueprint, redirect, render_template, request, url_for
from dndman.database.database import PFP_PATH, database
from dndman.logger import logger
from werkzeug.utils import secure_filename

import flask_login

profile = Blueprint(
    "profile", __name__, static_folder="static", template_folder="templates"
)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

@profile.route("/", methods=["GET", "POST"])
@flask_login.login_required
def profile_page():
    if request.method == "POST":
        
        if "pfp" not in request.files:
            return redirect(request.url)
        
        raw_pfp = request.files["pfp"]
        
        if allowed_file(raw_pfp.filename):
            pfp_path = PFP_PATH + flask_login.current_user.id + "." + secure_filename(raw_pfp.filename).rsplit('.', 1)[1].lower()
            raw_pfp.save("dndman/" + pfp_path)
            flask_login.current_user.pfp_path = pfp_path
            database.get_user(flask_login.current_user.id).pfp_path = pfp_path
            database.commit()
            return redirect(url_for("profile.profile_page"))

    logger.info(flask_login.current_user.pfp_path)

    return render_template(
        "profile/profile.html",
        username=flask_login.current_user.username,
        pfp=flask_login.current_user.pfp_path,
    )

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS