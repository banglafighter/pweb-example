from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD
from pwebe_basic.form.member_form import MemberCreateForm
from pwebe_basic.model.Person import Person


class FormService:
    form_data_crud: FormDataCRUD = FormDataCRUD(model=Person)

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
        return self.form_data_crud.render("form/create", form=form)

    def update(self, model_id: int):
        pass

    def details(self, model_id: int):
        pass

    def delete(self, model_id: int):
        pass

    def list(self):
        pass
