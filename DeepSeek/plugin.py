from supybot import utils, plugins, ircutils, callbacks
from supybot.commands import *

from supybot.i18n import PluginInternationalization, internationalizeDocstring
_ = PluginInternationalization('DeepSeek')

from openai import OpenAI


class DeepSeek(callbacks.Plugin):
    """DeepSeek API implementation."""
    threaded = True

    @internationalizeDocstring
    def msg(self, irc, msg, args, text):
        """<message>"""

        client = OpenAI(api_key=self.registryValue('api_key'),
                        base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful bot in IRC"},
                {"role": "user", "content": text},
            ],
            stream=False
        )
        content = response.choices[0].message.content
        for line in content.splitlines():
            if line:
                irc.reply(line, prefixNick=False)
    msg = wrap(msg, ["text"])


Class = DeepSeek
