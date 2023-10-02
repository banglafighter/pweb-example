from application.config.app_config import Config
from ppy_file_text import FileUtil


class AssetsConfig:
    fileHolder = FileUtil.join_path(Config.UPLOADED_STATIC_RESOURCES, "file-holder")
    formFile = FileUtil.join_path(Config.UPLOADED_STATIC_RESOURCES, "form-file")
