import requests
from supybot import utils, plugins, ircutils, callbacks
from supybot.commands import *
from supybot.i18n import PluginInternationalization, internationalizeDocstring


_ = PluginInternationalization('GisWeather')


class GisWeather(callbacks.Plugin):
    """Weather plugin according to Gismeteo data."""
    threaded = True

    def _get_loc_id(self, query: str) -> tuple[int,str]:
        payload = { 'lang': self.registryValue('language'),
                    'query': query, }
        headers = { 'X-Gismeteo-Token': self.registryValue('token'), }
        r = requests.get('https://api.gismeteo.net/v2/search/cities/',
                         params=payload, headers=headers)
        data = r.json()
        return ( data['response']['items'][0]['id'],
                 data['response']['items'][0]['name'], )

    def _get_weather(self, loc_id: int) -> dict:
        url = 'https://api.gismeteo.net/v2/weather/current/{}'.format(loc_id)
        payload = { 'lang': self.registryValue('language'), }
        headers = { 'X-Gismeteo-Token': self.registryValue('token'), }
        r = requests.get(url, params=payload, headers=headers)
        data = r.json()
        return data['response']

    @internationalizeDocstring
    def weather(self, irc, msg, args, query):
        """<location>

        Gets current weather of given location by Gismeteo data.
        """
        loc_id, loc_name = self._get_loc_id(query)
        data = self._get_weather(loc_id)

        template_data = {
            'loc': loc_name,
            'temp': data['temperature']['air']['C'],
            'temp_like': data['temperature']['comfort']['C'],
            'desc': data['description']['full'],
            'hum': data['humidity']['percent'],
            'pressure': data['pressure']['mm_hg_atm'],
            'wind_sp': data['wind']['speed']['m_s'],
        }
        reply = (self.registryValue('template').format(**template_data) +
                    _(' (according to Gismeteo data)')) # required!
        irc.reply(reply, to=msg.channel)
    weather = wrap(weather, ['text'])


Class = GisWeather


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
