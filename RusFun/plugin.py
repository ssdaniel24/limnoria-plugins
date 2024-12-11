import xml.etree.ElementTree as ET
from supybot.commands import *
from supybot import utils, plugins, ircutils, callbacks


class RusFun(callbacks.Plugin):
    """Развлекательный плагин, не несущий смысловую нагрузку."""
    threaded = True

    def horo(self, irc, msg, args, optlist, sign):
        """[--ero] <знак зодиака>

        Печатает сегодняшний гороскоп данного знака Зодиака. Флаг '--ero'
        переключает гороскоп на эротический.
        """
        sign = sign.lower()

        zodiac2latin = {
            'овен': 'aries',
            'телец': 'taurus',
            'близнецы': 'gemini',
            'рак': 'cancer',
            'лев': 'leo',
            'дева': 'virgo',
            'весы': 'libra',
            'скорпион': 'scorpio',
            'стрелец': 'sagittarius',
            'козерог': 'capricorn',
            'водолей': 'aquarius',
            'рыбы': 'pisces',
        }

        url = 'https://ignio.com/r/export/utf/xml/daily/com.xml'
        if 'ero' in (k for k,v in optlist):
            url = 'https://ignio.com/r/export/utf/xml/daily/ero.xml'

        resp = utils.web.getUrl(url).decode()
        root = ET.fromstring(resp)
        horo_ET = root.find('./{}/today'.format(zodiac2latin[sign]))
        irc.reply(horo_ET.text.strip())
    horo = wrap(horo, [
        getopts({ 'ero': '', }),
        ( 'literal', (
            'Овен', 'овен',
            'Телец', 'телец',
            'Близнецы', 'близнецы',
            'Рак', 'рак',
            'Лев', 'лев',
            'Дева', 'дева',
            'Весы', 'весы',
            'Скорпион', 'скорпион',
            'Стрелец', 'стрелец',
            'Козерог', 'козерог',
            'Водолей', 'водолей',
            'Рыбы', 'рыбы',
        ),)
    ])


Class = RusFun


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
