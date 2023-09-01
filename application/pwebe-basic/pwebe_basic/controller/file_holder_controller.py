from pweb import Blueprint
from pweb_form_rest import pweb_upload_endpoint
from pwebe_basic.dto.file_holder_dto import UploadAnyFileDTO, UploadPDFFileDTO, UploadDocFileDTO, UploadArchiveFileDTO, \
    UploadImageFileDTO, UploadCustomNameFileDTO, UploadPrefixNameFileDTO, UploadSizedFileDTO, DataAndUploadFileDTO
from pwebe_basic.service.file_holder_service import FileHolderService

url_prefix = "/api/v1/file-holder"
file_holder_controller = Blueprint(
    "file_holder_controller",
    __name__,
    url_prefix=url_prefix
)

file_holder_service = FileHolderService()


@file_holder_controller.route("/upload-any-file", methods=['POST'])
@pweb_upload_endpoint(request_obj=UploadAnyFileDTO, pweb_message_response=True)
def upload_any_file():
    return file_holder_service.upload_any_file()


@file_holder_controller.route("/upload-pdf-file", methods=['POST'])
@pweb_upload_endpoint(request_obj=UploadPDFFileDTO, pweb_message_response=True)
def upload_pdf_file():
    return file_holder_service.upload_pdf_file()


@file_holder_controller.route("/upload-doc-file", methods=['POST'])
@pweb_upload_endpoint(request_obj=UploadDocFileDTO, pweb_message_response=True)
def upload_doc_file():
    return file_holder_service.upload_doc_file()


@file_holder_controller.route("/upload-archive-file", methods=['POST'])
@pweb_upload_endpoint(request_obj=UploadArchiveFileDTO, pweb_message_response=True)
def upload_archive_file():
    return file_holder_service.upload_archive_file()


@file_holder_controller.route("/upload-image-file", methods=['POST'])
@pweb_upload_endpoint(request_obj=UploadImageFileDTO, pweb_message_response=True)
def upload_image_file():
    return file_holder_service.upload_image_file()


@file_holder_controller.route("/upload-custom-name-file", methods=['POST'])
@pweb_upload_endpoint(request_obj=UploadCustomNameFileDTO, pweb_message_response=True)
def upload_custom_name_file():
    return file_holder_service.upload_custom_name_file()


@file_holder_controller.route("/upload-prefix-name-file", methods=['POST'])
@pweb_upload_endpoint(request_obj=UploadPrefixNameFileDTO, pweb_message_response=True)
def upload_prefix_name_file():
    return file_holder_service.upload_prefix_name_file()


@file_holder_controller.route("/upload-sized-file", methods=['POST'])
@pweb_upload_endpoint(request_obj=UploadSizedFileDTO, pweb_message_response=True)
def upload_sized_file():
    return file_holder_service.upload_sized_file()


@file_holder_controller.route("/data-and-upload-file", methods=['POST'])
@pweb_upload_endpoint(request_obj=DataAndUploadFileDTO, pweb_message_response=True)
def data_and_upload_file():
    return file_holder_service.data_and_upload_file()
