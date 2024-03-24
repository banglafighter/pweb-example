from pweb import Blueprint
from pweb_extra.pws.pweb_socket import PWebSocket
from pweb_form_rest import ssr_ui_render

url_prefix = "/socket"
socket_controller = Blueprint(
    "socket_controller",
    __name__,
    url_prefix=url_prefix
)


@socket_controller.route("/", methods=['GET'])
def index():
    return ssr_ui_render(view_name="socket/index")


@socket_controller.route("/notify", methods=['GET'])
def notify():
    PWebSocket.notify("eventName", {"json": "Data"})
    return "Notified"
