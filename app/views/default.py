from flask import Blueprint

blueprint = Blueprint("index", __name__, url_prefix="/")


@blueprint.route("/", methods=["GET"])
def index():
    return "Simple web application prototype"
