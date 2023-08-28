from pweb import fields, APIBase, FileField


class PersonDTO(APIBase):
    first_name = fields.String(required=True, error_messages={"required": "Please enter first name"})
    last_name = fields.String(allow_none=None)
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})
    income = fields.Float(allow_none=None)
    image = FileField(allow_none=None)
