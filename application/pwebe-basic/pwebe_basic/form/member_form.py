from pweb import fields, FileField
from pweb_form_rest import PWebForm
from pweb_form_rest.common.pweb_custom_field import BaseEnum, EnumField


class Sex(BaseEnum):
    Male = "Male"
    Female = "Female"
    Not_Specified = "Not Specified"


class MemberDetailsForm(PWebForm):
    firstname = fields.String(required=True, error_messages={"required": "Please enter first name"})
    lastname = fields.String(allow_none=True)
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})
    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")
    age = fields.Integer(allow_none=True)
    dob = fields.Date(allow_none=True)
    image = FileField(allow_none=True).set_allowed_extension(["jpg", "png"])
    income = fields.Float(allow_none=True)
    sex = EnumField(Sex, required=True, error_messages={"required": "Please select sex"}, placeholder="Select Sex")
    bio = fields.String(type="textarea", placeholder="Enter Biography")
    technology = fields.String(allow_none=True)
    selectedCourse = fields.String(allow_none=True)

    # For Checkbox
    hasLaptop = fields.Boolean(allow_none=True, type="checkbox")
    hasPenDrive = fields.Boolean(allow_none=True)
    hasSmartPhone = fields.Boolean(allow_none=True)
    hasPowerBank = fields.String(allow_none=True)
