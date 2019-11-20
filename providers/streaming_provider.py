from netflix import Netflix_Potato
import credentials
from providers import brower_provider


class StreamingProvider:

    def __init__(self, settings):
        self.browser = settings.browser
        self.potato = settings.potato
        self.cr = settings.credentials

    def get_potato(self):
        if(self.potato == 'netflix'):
            return Netflix_Potato(self.cr, self.browser)


class StreamingProviderSettings:
    def __init__(self, potato, browser):
        # credentials
        cr = credentials.get_credentials(potato)
        self.credentials = cr
        self.potato = potato
        self.browser = brower_provider.get_brower(browser)
