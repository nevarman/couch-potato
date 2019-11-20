from netflix import Netflix_Potato
import credentials
from providers import brower_provider


class StreamingProvider:

    def __init__(self, settings):
        self.settings = settings

    def get_potato(self):
        if(self.settings.potato == 'netflix'):
            return Netflix_Potato(self.settings)
        # amazon prime ?...


class StreamingProviderSettings:
    def __init__(self, potato, browser):
        # credentials
        cr = credentials.get_credentials(potato)
        self.credentials = cr
        self.potato = potato
        self.browser = brower_provider.get_brower(browser)
