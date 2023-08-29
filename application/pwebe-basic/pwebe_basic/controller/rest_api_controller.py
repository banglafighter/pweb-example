from pweb import Blueprint, pweb_endpoint, pweb_paginate_endpoint
from pweb_form_rest import pweb_upload_endpoint
from pwebe_basic.dto.person_dto import PersonCreateDTO, PersonUpdateDTO, PersonDetailsDTO, PersonUploadDTO

url_prefix = "/api/v1/rest"
rest_api_controller = Blueprint(
    "rest_api_controller",
    __name__,
    url_prefix=url_prefix
)


@rest_api_controller.route("/create", methods=['POST'])
@pweb_endpoint(request_obj=PersonCreateDTO, pweb_message_response=True)
def create():
    return ""


@rest_api_controller.route("/details/<int:id>", methods=['GET'])
@pweb_endpoint(response_obj=PersonDetailsDTO)
def details(id: int):
    return ""


@rest_api_controller.route("/update", methods=['POST'])
@pweb_endpoint(request_obj=PersonUpdateDTO, pweb_message_response=True)
def update():
    return ""


@rest_api_controller.route("/delete/<int:id>", methods=['DELETE'])
@pweb_endpoint()
def delete(id: int):
    return ""


@rest_api_controller.route("/upload", methods=['POST'])
@pweb_upload_endpoint(request_obj=PersonUploadDTO, pweb_message_response=True)
def upload():
    return ""


@rest_api_controller.route("/list", methods=['GET'])
@pweb_paginate_endpoint(response_obj=PersonDetailsDTO)
def list():
    return ""
