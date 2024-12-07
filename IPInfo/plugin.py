import json
from country_codes import COUNTRY_CODES
from supybot import conf, utils, callbacks
from supybot.commands import *

def format_if_exist(string: str, target: str):
    """Formats string with target. If it does not exist, returns ''."""
    if target:
        return string.format(target)
    return ''

class IPInfo(callbacks.Plugin):
    """Plugin for working with https://ipinfo.io/"""
    threaded = True

    _api_url_template = 'https://ipinfo.io/{}?token={}'

    def fetch_ipinfo(self, ip):
        """Returns ipinfo dict"""
        url = self._api_url_template.format(ip, self.registryValue('token'))
        resp = utils.web.getUrl(url)
        return json.loads(resp.decode())

    def get(self, irc, msg, args, ip):
        """<ip>

        Shows IP address data from IPinfo.io.
        """
        conf.supybot
        data = self.fetch_ipinfo(ip)

        s = ip
        s += format_if_exist(' ({})', data.get('hostname'))
        s += ': '
        if data.get('country'):
            country = COUNTRY_CODES.get(data['country'])
            s += 'country: '
            if country:
                s += '{} ({})'.format(country, data['country'])
            else:
                s += data['country']
                self.log.error(f'Unknown country code: {data["country"]}')
        s += format_if_exist(', reg: {}', data.get('region'))
        s += format_if_exist(', city: {}', data.get('city'))
        s += format_if_exist(', org: {}', data.get('org'))
        if not s.endswith('.'):
            s += '.'

        irc.reply(s)
    get = wrap(get, ['ip'])

Class = IPInfo

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
