from supybot.test import *


class RusFunTestCase(PluginTestCase):
    plugins = ('RusFun',)

    def test_horo(self):
        self.assertNotError('horo Овен')
        self.assertNotError('horo дева')
        self.assertNotError('horo водолей')
        self.assertNotError('horo Рыбы')


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
