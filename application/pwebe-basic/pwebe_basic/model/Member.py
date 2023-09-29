from pweb_orm import PwebModel, pweb_orm


class Member(PwebModel):
    firstname = pweb_orm.Column("first_name", pweb_orm.String(150), nullable=False)
    lastname = pweb_orm.Column("last_name", pweb_orm.String(150))
    email = pweb_orm.Column("email", pweb_orm.String(120), nullable=False, unique=True)
    password = pweb_orm.Column("password", pweb_orm.String(100), nullable=False)
    age = pweb_orm.Column("age", pweb_orm.Integer)
    dob = pweb_orm.Column("dob", pweb_orm.Date())  # Date Picker
    image = pweb_orm.Column("image", pweb_orm.String(250))  # File With Validation
    income = pweb_orm.Column("income", pweb_orm.Float, default=0)
    sex = pweb_orm.Column("sex", pweb_orm.String(20), nullable=False)  # ENUM Select
    technology = pweb_orm.Column("technology", pweb_orm.String(40))  # Custom Select

    selectedCourse = pweb_orm.Column("selected_course", pweb_orm.String(40))  # Radio

    # these are for checkbox
    hasLaptop = pweb_orm.Column("has_laptop", pweb_orm.Boolean)
    hasPenDrive = pweb_orm.Column("has_pen_drive", pweb_orm.Boolean)
    hasSmartPhone = pweb_orm.Column("has_smart_phone", pweb_orm.Boolean)
    hasPowerBank = pweb_orm.Column("has_power_bank", pweb_orm.String(5))  # Yes / No

