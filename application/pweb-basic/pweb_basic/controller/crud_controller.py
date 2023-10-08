from pweb import Blueprint
from pweb_basic.model.Person import Person

url_prefix = "/crud"
crud_controller = Blueprint(
    "crud_controller",
    __name__,
    url_prefix=url_prefix
)


@crud_controller.route('/create')
def create():
    person = Person(firstname="First Name", lastname="Last Name", email="hmtmcse.com@gmail.com", age=22, income=500)
    person.save()
    response = "Data successfully Inserted"
    return response


@crud_controller.route('/update')
def update():
    person = Person.query.filter_by(id=1).first()
    if person:
        person.firstname = "FName Update"
        person.lastname = "LName Update"
        person.save()
    return "Data has been updated."


@crud_controller.route('/delete')
def delete():
    person = Person.query.filter_by(id=1).first()
    if person:
        person.delete()
    return "Record has been deleted"


@crud_controller.route('/list')
def list():
    response = ""
    persons = Person.query.all()
    for person in persons:
        response += person.firstname + " " + person.lastname + " " + person.email + "<br>"
    return response
