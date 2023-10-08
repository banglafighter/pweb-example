from pweb_orm import PwebModel, pweb_orm


class Person(PwebModel):
    firstname = pweb_orm.Column("first_name", pweb_orm.String(150), nullable=False)
    lastname = pweb_orm.Column("last_name", pweb_orm.String(150))
    email = pweb_orm.Column("email", pweb_orm.String(120), nullable=False)
    age = pweb_orm.Column("age", pweb_orm.Integer)
    image = pweb_orm.Column("image", pweb_orm.String(250))
    income = pweb_orm.Column("income", pweb_orm.Float, default=0)
