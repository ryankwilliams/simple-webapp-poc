from flask import Blueprint, render_template

blueprint = Blueprint("requests_view", __name__, url_prefix="/requests")


@blueprint.route("/create", methods=["GET"])
def index():
    return render_template("form.html")
