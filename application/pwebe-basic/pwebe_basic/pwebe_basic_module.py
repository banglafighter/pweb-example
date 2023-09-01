from pweb import PWebComponentRegister
from pwebe_basic.controller.basic_controller import basic_controller
from pwebe_basic.controller.crud_controller import crud_controller
from pwebe_basic.controller.file_holder_controller import file_holder_controller
from pwebe_basic.controller.rest_api_controller import rest_api_controller
from pwebe_basic.controller.saas_controller import saas_controller


class PWebBasicModule(PWebComponentRegister):

    def run_on_start(self, pweb_app):
        pass

    def register_model(self, pweb_db):
        pass

    def register_controller(self, pweb_app):
        pweb_app.register_blueprint(basic_controller)
        pweb_app.register_blueprint(crud_controller)
        pweb_app.register_blueprint(saas_controller)
        pweb_app.register_blueprint(rest_api_controller)
        pweb_app.register_blueprint(file_holder_controller)
