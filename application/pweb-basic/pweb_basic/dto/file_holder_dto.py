from marshmallow import fields
from pweb_form_rest import FileField
from pweb_form_rest.schema.pweb_rest_schema import PWebRestDTO
from pweb_basic.model.FileHolder import FileHolder


class UploadAnyFileDTO(PWebRestDTO):
    anyFile = FileField(required=True, error_messages={"required": "Please enter any kind of file"})

    class Meta:
        model = FileHolder
        load_instance = True


class UploadPDFFileDTO(PWebRestDTO):
    pdfFile = FileField(required=True, error_messages={"required": "Please enter PDF File"}).set_allowed_extension(["pdf"])

    class Meta:
        model = FileHolder
        load_instance = True


class UploadDocFileDTO(PWebRestDTO):
    docFile = FileField(required=True, error_messages={"required": "Please enter Document File"}).set_allowed_extension(["doc", "docx", "xlsx"])

    class Meta:
        model = FileHolder
        load_instance = True


class UploadArchiveFileDTO(PWebRestDTO):
    archiveFile = FileField(required=True, error_messages={"required": "Please enter Archive File"}).set_allowed_extension(["zip", "7z"])

    class Meta:
        model = FileHolder
        load_instance = True


class UploadImageFileDTO(PWebRestDTO):
    imageFile = FileField(required=True, error_messages={"required": "Please enter Image File"}).set_allowed_extension(["jpg", "png", "jpeg"])

    class Meta:
        model = FileHolder
        load_instance = True


class UploadCustomNameFileDTO(PWebRestDTO):
    customNameFile = FileField(required=True, error_messages={"required": "Please enter any kind of file"})

    class Meta:
        model = FileHolder
        load_instance = True


class UploadPrefixNameFileDTO(PWebRestDTO):
    anyFile = FileField(required=True, error_messages={"required": "Please enter any kind of file"}).set_save_prefix("prefix")

    class Meta:
        model = FileHolder
        load_instance = True


class UploadSizedFileDTO(PWebRestDTO):
    anyFile = FileField(required=True, error_messages={"required": "Please enter file less than 100KB"}).set_max_size_kb(100)

    class Meta:
        model = FileHolder
        load_instance = True


class DataAndUploadFileDTO(PWebRestDTO):
    anyFile = FileField(required=True, error_messages={"required": "Please enter any kind of file"})
    alterText = fields.String(required=True, error_messages={"required": "Please enter alter text"})
    title = fields.String(allow_none=True)

    class Meta:
        model = FileHolder
        load_instance = True
