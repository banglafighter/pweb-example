from pweb import PWebAppConfig
from pweb_form_rest import PWebSSRUIHelper
from pweb_ssr import SSRTemplateAssets
from pwebe_basic.common.app_ssr_ui_helper import AppSSRUIHelper


class Config(PWebAppConfig):
    SWAGGER_TITLE: str = "Swagger Example App"
    SSR_UI_HELPER: PWebSSRUIHelper = AppSSRUIHelper()

    DEFAULT_TEMPLATE_ASSETS: SSRTemplateAssets = SSRTemplateAssets(
        name="example",
        import_name=__name__,
        template_folder="../template-assets/templates",
        static_url_path="../template-assets/assets",
        static_folder="assets"
    )
