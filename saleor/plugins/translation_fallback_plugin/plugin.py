from saleor.plugins.base_plugin import BasePlugin
from saleor.graphql.page.types import Page


class TranslationFallbackPlugin(BasePlugin):
    PLUGIN_ID = "translation_fallback"
    PLUGIN_NAME = "Translation Fallback Plugin"
    DEFAULT_ACTIVE = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


