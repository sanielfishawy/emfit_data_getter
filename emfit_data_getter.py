#pylint: disable=invalid-name, line-too-long, anomalous-backslash-in-string
import urllib.request
import re
import time
from emfit_ip_finder import EmfitIpFinder


class EmfitDataGetter:
    '''
        Use to get heart rate and respiration rate from Emfit device on local network.
        Instantiation is expensive because discover of emfit ip address can take as long as
        20 seconds.
        Maintain an instance for rapid successive reading of data.
    '''
    DATA_PAGE = '/shortdvm.htm'

    def __init__(self):
        self.ip_finder = EmfitIpFinder()
        self.emfit_ip_address = self.ip_finder.get_ip()

    def get_heart_rate(self):
        return self._get_hr_from_html(self._get_html())

    def get_respiration_rate(self):
        return self._get_rr_from_html(self._get_html())

    def _get_html(self):
        with urllib.request.urlopen('http://' + self.emfit_ip_address + EmfitDataGetter.DATA_PAGE) as response:
            html = response.read()
        return html.decode('UTF-8')

    def _get_hr_from_html(self, htm):
        match = re.compile('HR:.+?(<\/)').search(htm)
        match = re.compile('(.+>) *(.*)<').search(match[0])
        return self._get_float_from_string(match[2])

    def _get_rr_from_html(self, htm):
        match = re.compile('RR:.+?(<\/)').search(htm)
        match = re.compile('(.+>) *(.*)<').search(match[0])
        return self._get_float_from_string(match[2])

    def _get_float_from_string(self, txt):
        result = None

        try:
            result = float(txt)
        except ValueError:
            pass

        return result

if __name__ == '__main__':
    data_getter = EmfitDataGetter()
    while True:
        print(data_getter.get_heart_rate())
        print(data_getter.get_respiration_rate())
        time.sleep(2)
