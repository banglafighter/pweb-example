from pweb import Blueprint
from pweb_basic.service.ssr_service import SSRService

url_prefix = "/ssr"
ssr_controller = Blueprint(
    "ssr_controller",
    __name__,
    url_prefix=url_prefix
)

ssr_service = SSRService()


@ssr_controller.route("/", methods=['GET'])
def index():
    return ssr_service.index()
