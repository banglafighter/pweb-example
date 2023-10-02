from application.config.assets_config import AssetsConfig
from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD
from pwebe_basic.form.member_form import MemberCreateForm, MemberUpdateForm
from pwebe_basic.model.Member import Member
from pweb import url_for


class FormService:
    form_data_crud: FormDataCRUD = FormDataCRUD(model=Member)

    def _get_technology_options(self):
        return {
            "Computer": "Computer",
            "Electrical": "Electrical",
            "Mechanical": "Mechanical",
            "Civil": "Civil",
            "Electronics": "Electronics",
        }

    def create(self):
        params = {"button": "Create", "action": url_for("form_controller.create")}
        form = MemberCreateForm()
        form.set_select_option("technology", select_options=self._get_technology_options())
        return self.form_data_crud.create(view_name="form/form", form=form, redirect_url=url_for("form_controller.list"), params=params, upload_path=AssetsConfig.formFile)

    def update(self, model_id: int):
        params = {"button": "Update", "action": url_for("form_controller.update", id=model_id)}
        form = MemberUpdateForm()
        form.set_select_option("technology", select_options=self._get_technology_options())
        return self.form_data_crud.update(view_name="form/form", model_id=model_id, update_form=form, redirect_url=url_for("form_controller.list"), params=params, upload_path=AssetsConfig.formFile)

    def details(self, model_id: int):
        return self.form_data_crud.details("form/details", model_id=model_id, redirect_url=url_for("form_controller.list"))

    def delete(self, model_id: int):
        return self.form_data_crud.delete(model_id=model_id, redirect_url=url_for("form_controller.list"))

    def list(self):
        search_fields: list = ["firstname", "lastname", "email", "technology"]
        return self.form_data_crud.paginated_list(view_name="form/list", search_fields=search_fields)
