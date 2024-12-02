from supybot.test import *


class RateCBRTestCase(PluginTestCase):
    plugins = ('RateCBR',)

    def testGettingRate(self):
        self.assertNotError('rate')
        self.assertNotError('rate EUR')
        self.assertNotError('rate CNY')
        self.assertNotError('rate UAH')
        self.assertNotError('rate BYN')

    def testGettingAvailableCurrencies(self):
        self.assertNotError('currencies')


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
