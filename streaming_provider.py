from netflix import Netflix_Potato
import credentials


class StreamingProvider:

    def __init__(self, browser, potato):
        self.browser = browser
        self.potato = potato

    def get_potato(self):
        cr = credentials.get_credentials(self.potato)
        if(self.potato == 'netflix'):
            return Netflix_Potato(cr, self.browser)
