from pweb import PWebModuleRegister
from pweb_auth import PWebAuthModule
from pweb_basic.pweb_basic_module import PWebBasicModule
from pweb_ssr.pweb_ssr_module import PWebSSRModule
from pweb_ui.pweb_ui_module import PWebUIModule


class Register(PWebModuleRegister):

    def get_module_list(self) -> list:
        return [
            PWebSSRModule,
            PWebAuthModule,
            PWebBasicModule,
            PWebUIModule,
        ]
