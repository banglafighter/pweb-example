from pweb import Blueprint

url_prefix = "/"
basic_controller = Blueprint(
    "basic_controller",
    __name__,
    url_prefix=url_prefix
)


@basic_controller.route("/", methods=['GET'])
def index():
    return "Index Page"
