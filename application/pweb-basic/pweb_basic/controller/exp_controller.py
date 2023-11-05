from pweb import Blueprint
from pweb_form_rest import pweb_endpoint


class ExpController:

    def __init__(self, url_prefix="/exp"):
        self.controller = Blueprint(
            "exp_controller",
            __name__,
            url_prefix=url_prefix
        )

    def index(self, url="/index"):
        @pweb_endpoint()
        def index_action():
            return "Index action"

        return self.controller.add_url_rule(url, "index", index_action)

    @staticmethod
    def init_controller(pweb_app):
        exp = ExpController()
        exp.index()
        pweb_app.register_blueprint(exp.controller)
