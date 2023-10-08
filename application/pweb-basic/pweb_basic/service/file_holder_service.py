from application.config.assets_config import AssetsConfig
from pweb_form_rest import FileDataCRUD
from pweb_basic.dto.file_holder_dto import UploadAnyFileDTO, UploadPDFFileDTO, UploadDocFileDTO, UploadArchiveFileDTO, \
    UploadImageFileDTO, UploadCustomNameFileDTO, UploadPrefixNameFileDTO, UploadSizedFileDTO, DataAndUploadFileDTO
from pweb_basic.model.FileHolder import FileHolder


class FileHolderService:
    file_data_crud = FileDataCRUD(model=FileHolder())

    def upload_any_file(self):
        return self.file_data_crud.upload_file_data(request_dto=UploadAnyFileDTO(), upload_path=AssetsConfig.fileHolder)

    def upload_pdf_file(self):
        return self.file_data_crud.upload_file_data(request_dto=UploadPDFFileDTO(), upload_path=AssetsConfig.fileHolder)

    def upload_doc_file(self):
        return self.file_data_crud.upload_file_data(request_dto=UploadDocFileDTO(), upload_path=AssetsConfig.fileHolder)

    def upload_archive_file(self):
        return self.file_data_crud.upload_file_data(request_dto=UploadArchiveFileDTO(), upload_path=AssetsConfig.fileHolder)

    def upload_image_file(self):
        return self.file_data_crud.upload_file_data(request_dto=UploadImageFileDTO(), upload_path=AssetsConfig.fileHolder)

    def upload_custom_name_file(self):
        override_names: dict = {"customNameFile": "custom-name-file"}
        return self.file_data_crud.upload_file_data(request_dto=UploadCustomNameFileDTO(), upload_path=AssetsConfig.fileHolder, override_names=override_names)

    def upload_prefix_name_file(self):
        return self.file_data_crud.upload_file_data(request_dto=UploadPrefixNameFileDTO(), upload_path=AssetsConfig.fileHolder)

    def upload_sized_file(self):
        return self.file_data_crud.upload_file_data(request_dto=UploadSizedFileDTO(), upload_path=AssetsConfig.fileHolder)

    def data_and_upload_file(self):
        return self.file_data_crud.upload_file_data(request_dto=DataAndUploadFileDTO(), upload_path=AssetsConfig.fileHolder)
