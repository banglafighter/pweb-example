from pweb_form_rest import PWebSSRUIHelper


class CustomFunctionForUI:

    def print(self):
        return "Print Something in UI"


class AppSSRUIHelper(PWebSSRUIHelper):
    def get_helper(self) -> dict:
        return {
            "custom": CustomFunctionForUI()
        }
