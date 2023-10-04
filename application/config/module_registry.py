from pweb import PWebModuleRegister
from pweb_auth import PWebAuthModule
from pweb_ssr.pweb_ssr_module import PWebSSRModule
from pweb_ui.pweb_ui_module import PWebUIModule
from pwebe_basic.pwebe_basic_module import PWebBasicModule


class Register(PWebModuleRegister):

    def get_module_list(self) -> list:
        return [
            PWebUIModule,
            PWebBasicModule,
            PWebSSRModule,
            PWebAuthModule
        ]
