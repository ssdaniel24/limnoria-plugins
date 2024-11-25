from supybot import utils, plugins, ircutils, callbacks
from supybot.commands import *
from supybot.i18n import PluginInternationalization


class RateCBR(callbacks.Plugin):
    """Показывает актуальные курсы валют с sbr.ru"""
    threaded = True


Class = RateCBR


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
