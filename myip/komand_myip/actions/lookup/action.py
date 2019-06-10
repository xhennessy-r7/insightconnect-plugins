import komand
from .schema import LookupInput, LookupOutput
# Custom imports below
import requests


class Lookup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup',
                description='Obtain your public routable IP address',
                input=LookupInput(),
                output=LookupOutput())

    def run(self, params={}):
        try:
            r = requests.get('https://api.myip.com')
            r.raise_for_status()
            out = r.json()
        except Exception as e:
            self.logger.error(e)
            raise

        return out

    def test(self):
        try:
            r = requests.get('https://api.myip.com')
            r.raise_for_status()
            out = r.json()
        except Exception as e:
            self.logger.error(e)
            raise
        return out
