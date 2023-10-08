from pweb_form_rest import ssr_ui_render
from pweb_basic.form.member_form import MemberDetailsForm


class SSRService:

    def index(self):
        form = MemberDetailsForm()
        return ssr_ui_render(view_name="ssr/index", form=form)
