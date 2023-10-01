from marshmallow import validates_schema
from pweb import fields, FileField
from pweb_form_rest import PWebForm
from pweb_form_rest.common.pweb_custom_field import BaseEnum, EnumField
from pweb_orm import PWebORMUtil
from pwebe_basic.model.Member import Member


class Sex(BaseEnum):
    Male = "Male"
    Female = "Female"
    Not_Specified = "Not Specified"


class MemberDetailsForm(PWebForm):
    firstname = fields.String(required=True, error_messages={"required": "Please enter first name"})
    lastname = fields.String(allow_none=True, helpText="You may ignore it.")
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})
    age = fields.Integer(allow_none=True)
    dob = fields.Date(allow_none=True, label="Date of Birth")
    image = FileField(allow_none=True).set_allowed_extension(["jpg", "png"])
    income = fields.Float(required=True, error_messages={"required": "Please enter income"})
    sex = EnumField(Sex, required=True, error_messages={"required": "Please select sex"}, placeholder="Select Sex")
    bio = fields.String(type="textarea", placeholder="Enter Biography", allow_none=True)
    selectedCourse = fields.String(allow_none=True, radioItem={"python-web": "Python & Web Development", "java-web": "Java & Web Development"}, type="radio")

    technology = fields.String(allow_none=True, type="select", placeholder="Select Technology")

    # For Checkbox
    hasLaptop = fields.Boolean(allow_none=True, type="checkbox")
    hasPenDrive = fields.Boolean(allow_none=True, type="checkbox")
    hasSmartPhone = fields.Boolean(allow_none=True, type="checkbox")
    hasPowerBank = fields.String(allow_none=True, type="checkbox")

    @validates_schema
    def validates_schema(self, data, **kwargs):
        PWebORMUtil.enum_to_string(data, "sex")


class MemberCreateForm(MemberDetailsForm):
    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")

    class Meta:
        model = Member
        load_instance = True


class MemberUpdateForm(MemberDetailsForm):
    class Meta:
        model = Member
        load_instance = True

    id = fields.Integer(required=True, error_messages={"required": "Please enter id"}, type="hidden", isLabel=False)
