import random

from application.config.app_config import Config
from ppy_file_text import FileUtil
from pweb import Blueprint, pweb_orm, request
from pweb_orm import PWebSaaS
from pweb_basic.model.Person import Person

url_prefix = "/saas"
saas_controller = Blueprint(
    "saas_controller",
    __name__,
    url_prefix=url_prefix
)


@saas_controller.route("/", methods=['GET'])
def index():
    return "Index Page"


@saas_controller.route('/init-tenant')
def init_tenant():
    response = "Tenant Initialized"
    pweb_orm.register_tenant("db1", 'sqlite:///' + FileUtil.join_path(Config.BASE_DIR, 'db1.sqlite3'))
    pweb_orm.register_tenant("db2", 'sqlite:///' + FileUtil.join_path(Config.BASE_DIR, 'db2.sqlite3'))
    pweb_orm.register_tenant("db3", 'sqlite:///' + FileUtil.join_path(Config.BASE_DIR, 'db3.sqlite3'))
    return response


@saas_controller.route('/remove-tenant')
def remove_tenant():
    tkey = request.args.get("tkey")
    if tkey and pweb_orm.remove_tenant(tkey):
        return "Tenant Removed"
    return "Unable to remove tenant"


@saas_controller.route('/insert')
def insert():
    tkey = request.args.get("tkey", default="default")
    PWebSaaS.set_tenant_key(tkey)
    index = random.randint(0, 999)
    person = Person(first_name="First Name", last_name="Last Name", email=f"email-{tkey}-{index}@gmail.com", age=22, income=index)
    person.save()
    return f"Inserted to tenant {tkey}"
