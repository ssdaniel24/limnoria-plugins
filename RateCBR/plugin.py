from supybot.commands import *
from supybot import utils, callbacks
import xml.etree.ElementTree as ET


SUPPORTED_CURRENCIES = {
    'BYN': '🇧🇾', # Беларусь
    'VND': '🇻🇳', # Вьетнам
    'USD': '🇺🇸', # Америка
    'EUR': '🇪🇺', # Евросоюз
    'KZT': '🇰🇿', # Казахстан
    'CNY': '🇨🇳', # Китай
    'UAH': '🇺🇦', # Украина
    'JPY': '🇯🇵', # Япония
}

class RateCBR(callbacks.Plugin):
    """Показывает актуальные курсы валют с sbr.ru"""

    threaded = True
    _api_url = 'https://www.cbr.ru/scripts/XML_daily.asp' # win-1251

    def rate(self, irc, msg, args, currency):
        """[валюта XXX]

        Показывает текущий курс валюты XXX по отношению к рублю. XXX -
        её трёхбуквенный код. По умолчанию 'USD' - доллары США.
        Посмотреть поддерживаемые коды валют можно командой 'currencies'.
        """
        if not currency:
            currency = 'USD'
        resp = utils.web.getUrl(self._api_url).decode('cp1251')
        root = ET.fromstring(resp)
        for valute in root:
            code = valute.find('CharCode').text
            if code == currency:
                data = {
                    'code': code,
                    'nominal': valute.find('Nominal').text,
                    'name': valute.find('Name').text,
                    'value': valute.find('Value').text,
                }
                irc.reply(self.registryValue('template').format(**data),
                          to=msg.channel)
                return
        irc.error('Данная валюта не найдена!') # this mustn't happen
    rate = wrap(rate, [
        optional(
            ('literal', list(SUPPORTED_CURRENCIES.keys())),
        ),
    ])

    def currencies(self, irc, msg, args):
        """не принимает аргументов

        Печатает поддерживаемые валюты.
        """
        currencies = []
        for code, flag in SUPPORTED_CURRENCIES.items():
            currencies.append(f'{flag} - {code}')
        irc.reply(', '.join(currencies))
    currencies = wrap(currencies)


Class = RateCBR


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
