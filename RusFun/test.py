from supybot.test import *


class RusFunTestCase(PluginTestCase):
    plugins = ('RusFun',)

    def test_horo(self):
        self.assertNotError('horo Овен')
        self.assertNotError('horo дева')
        self.assertNotError('horo водолей')
        self.assertNotError('horo Рыбы')
        self.assertNotError('horo --ero Стрелец')
        self.assertNotError('horo --ero рак')
        self.assertNotError('horo --ero Лев')
        self.assertNotError('horo --ero телец')


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
