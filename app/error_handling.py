from flask import Blueprint
from flask import abort, render_template, redirect

error_bp = Blueprint("errors", __name__)

@error_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@error_bp.app_errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500