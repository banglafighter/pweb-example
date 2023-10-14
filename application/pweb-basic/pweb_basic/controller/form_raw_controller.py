from pweb import Blueprint, flash
from pweb_basic.form.member_form import MemberCreateForm
from pweb_form_rest import ssr_ui_render

url_prefix = "/form-raw"
form_raw_controller = Blueprint(
    "form_raw_controller",
    __name__,
    url_prefix=url_prefix
)


@form_raw_controller.route("/", methods=['GET', 'POST'])
def registration():
    form = MemberCreateForm()
    if form.is_valid_data():
        flash("Valid data submitted", "success")
    return ssr_ui_render(view_name="form-raw/registration", form=form)
