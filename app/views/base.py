from flask import Blueprint

blueprint = Blueprint("base_view", __name__, url_prefix="/")


@blueprint.route("/", methods=["GET"])
def index():
    return "Simple web application prototype"
