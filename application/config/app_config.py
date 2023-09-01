from pweb import PWebAppConfig
from pweb_ssr import SSRTemplateAssets


class Config(PWebAppConfig):
    SWAGGER_TITLE: str = "Swagger Example App"

    DEFAULT_TEMPLATE_ASSETS: SSRTemplateAssets = SSRTemplateAssets(
        name="example",
        import_name=__name__,
        template_folder="../template-assets/templates",
        static_url_path="../template-assets/assets",
        static_folder="assets"
    )
