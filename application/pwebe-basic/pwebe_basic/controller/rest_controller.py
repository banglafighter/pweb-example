from pweb import Blueprint

url_prefix = "/"
rest_controller = Blueprint(
    "rest_controller",
    __name__,
    url_prefix=url_prefix
)


@rest_controller.route("/", methods=['GET'])
def index():
    return "Index Page"
