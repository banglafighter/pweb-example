from pweb import Blueprint
from pweb_form_rest import ssr_ui_render
from pwebe_basic.service.form_service import FormService

url_prefix = "/form"
form_controller = Blueprint(
    "form_controller",
    __name__,
    url_prefix=url_prefix
)

form_service = FormService()


@form_controller.route("/create", methods=['POST', 'GET'])
def create():
    return form_service.create()


@form_controller.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id: int = None):
    return form_service.update(id)


@form_controller.route("/delete/<int:id>", methods=['GET'])
def delete(id: int):
    return form_service.delete(id)


@form_controller.route("/list", methods=['GET'])
def list():
    return form_service.list()


@form_controller.route("/custom-helper", methods=['GET'])
def custom_helper():
    return ssr_ui_render(view_name="form/custom-helper")
