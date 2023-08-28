from pweb import PWebModuleRegister
from pwebe_basic.pwebe_basic_registry import PWebBasicRegistry


class Register(PWebModuleRegister):

    def get_module_list(self) -> list:
        return [
            PWebBasicRegistry
        ]
