from pweb_orm import PwebModel, pweb_orm


class FileHolder(PwebModel):
    title = pweb_orm.Column("title", pweb_orm.String(100))
    alterText = pweb_orm.Column("alter_text", pweb_orm.String(100))
    pdfFile = pweb_orm.Column("pdf_file", pweb_orm.String(250))
    docFile = pweb_orm.Column("doc_file", pweb_orm.String(250))
    archiveFile = pweb_orm.Column("archive_file", pweb_orm.String(250))
    anyFile = pweb_orm.Column("any_file", pweb_orm.String(250))
    imageFile = pweb_orm.Column("image_file", pweb_orm.String(250))
    customNameFile = pweb_orm.Column("custom_name_file", pweb_orm.String(250))
