from flask import Blueprint, request
from flask_cors import cross_origin

from app.constants import API_PREFIX

blueprint = Blueprint(
    "requests",
    __name__,
    url_prefix=f"{API_PREFIX}/requests"
)


@blueprint.route("/create", methods=["POST"])
@cross_origin()
def create():
    subject = request.form['subject']
    description = request.form['description']
    attachments = request.files.getlist("attachments")

    for file in attachments:
        file.save(f"/tmp/{file.filename}")

    return f"Request: {subject}:{description} added!"
