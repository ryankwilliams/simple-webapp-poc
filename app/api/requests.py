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
    # http -f POST http://0.0.0.0:8081/app/api/v1/requests/create \
    # subject=subject description=description attachments@file.txt
    subject = request.form['subject']
    description = request.form['description']
    attachments = request.files.getlist("attachments")

    for file in attachments:
        file.save(f"/tmp/{file.filename}")

    return f"Your request has been created!"
