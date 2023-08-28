from pweb import Blueprint, pweb_endpoint, pweb_paginate_endpoint
from pweb_form_rest import pweb_upload_endpoint
from pwebe_basic.dto.person_dto import PersonCreateDTO, PersonUpdateDTO, PersonDetailsDTO, PersonUploadDTO

url_prefix = "/"
rest_controller = Blueprint(
    "rest_controller",
    __name__,
    url_prefix=url_prefix
)


@rest_controller.route("/create", methods=['POST'])
@pweb_endpoint(request_obj=PersonCreateDTO, pweb_message_response=True)
def create():
    return ""


@rest_controller.route("/details/<int:id>", methods=['GET'])
@pweb_endpoint(response_obj=PersonDetailsDTO)
def details(id: int):
    return ""


@rest_controller.route("/update", methods=['POST'])
@pweb_endpoint(request_obj=PersonUpdateDTO, pweb_message_response=True)
def update():
    return ""


@rest_controller.route("/delete/<int:id>", methods=['DELETE'])
@pweb_endpoint()
def delete(id: int):
    return ""


@rest_controller.route("/upload", methods=['POST'])
@pweb_upload_endpoint(response_obj=PersonUploadDTO)
def upload():
    return ""


@rest_controller.route("/list", methods=['GET'])
@pweb_paginate_endpoint(response_obj=PersonDetailsDTO)
def list():
    return ""
