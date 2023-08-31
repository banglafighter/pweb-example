from pweb import RESTDataCRUD
from pwebe_basic.dto.person_dto import PersonCreateDTO, PersonDetailsDTO, PersonUpdateDTO
from pwebe_basic.model.Person import Person


class PersonRESTService:
    rest_data_crud = RESTDataCRUD(model=Person)

    def create(self):
        return self.rest_data_crud.create(request_dto=PersonCreateDTO())

    def details(self, model_id: int):
        return self.rest_data_crud.details(model_id=model_id, response_dto=PersonDetailsDTO())

    def update(self):
        return self.rest_data_crud.update(request_dto=PersonUpdateDTO())

    def list(self):
        search_fields = []
        return self.rest_data_crud.paginated_list(response_dto=PersonDetailsDTO(), search_fields=search_fields)

    def delete(self, model_id: int):
        return self.rest_data_crud.delete(model_id=model_id)
