from pweb_orm import PwebModel, pweb_orm


class Person(PwebModel):
    first_name = pweb_orm.Column(pweb_orm.String(150), nullable=False)
    last_name = pweb_orm.Column(pweb_orm.String(150))
    email = pweb_orm.Column(pweb_orm.String(120), nullable=False)
    age = pweb_orm.Column(pweb_orm.Integer)
    income = pweb_orm.Column(pweb_orm.Float, default=0)
