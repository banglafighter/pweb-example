from pweb import PWebComponentRegister
from pwebe_basic.controller.basic_controller import basic_controller
from pwebe_basic.controller.crud_controller import crud_controller


class PWebEBasicRegistry(PWebComponentRegister):

    def run_on_start(self, pweb_app):
        pass

    def register_model(self, pweb_db):
        pass

    def register_controller(self, pweb_app):
        pweb_app.register_blueprint(basic_controller)
        pweb_app.register_blueprint(crud_controller)
