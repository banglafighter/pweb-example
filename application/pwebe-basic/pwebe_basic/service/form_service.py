from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD
from pwebe_basic.model.Person import Person


class FormService:
    form_data_crud: FormDataCRUD = FormDataCRUD(model=Person)

    def create(self):
        return self.form_data_crud.render("form/create")

    def update(self, model_id: int):
        pass

    def details(self, model_id: int):
        pass

    def delete(self, model_id: int):
        pass

    def list(self):
        pass
