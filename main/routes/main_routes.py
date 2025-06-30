from flask import Blueprint, request, session, render_template, redirect, url_for
from flask_babel import _, force_locale
from ..i18n_runtime import get_locale

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
@main_bp.route("/index")
def index():
    with force_locale(get_locale()):
        return render_template("index.html.j2")

@main_bp.route("/set_language/<lang>")
def set_language(lang):
    session["lang"] = lang
    return redirect(request.referrer or url_for("main.index"))
