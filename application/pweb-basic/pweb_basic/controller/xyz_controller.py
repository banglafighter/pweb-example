from datetime import date, datetime
from ppy_common import DateUtil
from pweb import Blueprint

url_prefix = "/xyz"
xyz_controller = Blueprint(
    "xyz_controller",
    __name__,
    url_prefix=url_prefix
)


@xyz_controller.route("/", methods=['GET'])
def index():
    return "Index Page"


@xyz_controller.route("/date-formatting", methods=['GET'])
def date_formatting():
    data_str = DateUtil.datetime_to_format_string(date_time=date.today())
    datatime_str = DateUtil.datetime_to_format_string(date_time=datetime.now())
    return f"Date string: {data_str}, Datetime string: {datatime_str}"

