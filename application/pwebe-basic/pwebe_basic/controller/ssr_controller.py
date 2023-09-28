from pweb import Blueprint
from pweb_form_rest import ssr_ui_render

url_prefix = "/ssr"
ssr_controller = Blueprint(
    "ssr_controller",
    __name__,
    url_prefix=url_prefix
)


@ssr_controller.route("/", methods=['GET'])
def index():
    return ssr_ui_render(view_name="ssr/index")
