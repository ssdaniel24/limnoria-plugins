from supybot.test import *


class GisWeatherTestCase(PluginTestCase):
    plugins = ('GisWeather',)

    def test_weather_getting(self):
        self.assertNotError('weather Moscow')
        self.assertNotError('weather Minsk')
        self.assertNotError('weather Oymyakon')


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
