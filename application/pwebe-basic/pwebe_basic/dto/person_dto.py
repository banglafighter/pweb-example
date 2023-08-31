from pweb import fields, FileField
from pweb_form_rest.schema.pweb_rest_schema import PWebRestDTO
from pwebe_basic.model.Person import Person


class PersonDetailsDTO(PWebRestDTO):
    firstname = fields.String(required=True, error_messages={"required": "Please enter first name"})
    lastname = fields.String(allow_none=True)
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})
    income = fields.Float(allow_none=True)


class PersonCreateDTO(PersonDetailsDTO):
    class Meta:
        model = Person
        load_instance = True


class PersonUpdateDTO(PersonDetailsDTO):
    class Meta:
        model = Person
        load_instance = True

    id = fields.Integer(required=True, error_messages={"required": "Please enter id"})


class PersonUploadDTO(PWebRestDTO):
    image = FileField(allow_none=True)
    id = fields.Integer(required=True, error_messages={"required": "Please enter id"})

    class Meta:
        model = Person
        load_instance = True
