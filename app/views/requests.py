from flask import Blueprint, request
from flask_cors import cross_origin

blueprint = Blueprint("requests", __name__, url_prefix="/requests")


@blueprint.route("/", methods=["GET"])
def index():
    return "View handling all request operations"


@blueprint.route("/new", methods=["POST"])
@cross_origin()
def new():
    subject = request.form['subject']
    description = request.form['description']
    attachments = request.files.getlist("attachments")

    for file in attachments:
        file.save(f"/tmp/{file.filename}")

    return f"Request: {subject}:{description} added!"
