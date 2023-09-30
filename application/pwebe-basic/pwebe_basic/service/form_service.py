from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD
from pwebe_basic.form.member_form import MemberCreateForm
from pwebe_basic.model.Member import Member


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
        form = MemberCreateForm()
        form.set_select_option("technology", select_options=self._get_technology_options())
        return self.form_data_crud.create(view_name="form/create", form=form)

    def update(self, model_id: int):
        pass

    def details(self, model_id: int):
        pass

    def delete(self, model_id: int):
        pass

    def list(self):
        return self.form_data_crud.paginated_list(view_name="form/list")
