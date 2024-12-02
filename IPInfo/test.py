from supybot.test import *


class IPInfoTestCase(PluginTestCase):
    plugins = ('IPInfo',)

    def test_getting(self):
        self.assertNotError('get 1.1.1.1')
        self.assertNotError('get 8.8.8.8')
        self.assertNotError('get 77.88.8.8')


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
