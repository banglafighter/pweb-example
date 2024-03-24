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
    PWebSocket.notify("eventName", "String Notification")
    return "Notified"


@socket_controller.route("/notify-dict", methods=['GET'])
def notify_dict():
    PWebSocket.notify("eventName", {"dict": "Dictionary Notification"})
    return "Notified Dict"


@socket_controller.route("/notify-message", methods=['GET'])
def notify_message():
    PWebSocket.notify_message("Message Notification")
    return "Notified Message"


def plain_text(message):
    print(f"Called PlainText: {message}")


def json_data(json_data):
    print(type(json_data))
    print(f"Called JSON Data: {json_data}")


@socket_controller.route("/register-event", methods=['GET'])
def register_event():
    PWebSocket.register_event("plainText", plain_text)
    PWebSocket.register_event("jsonData", json_data)
    return "Register Event"
