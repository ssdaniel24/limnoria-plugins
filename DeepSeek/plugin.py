from supybot import utils, plugins, ircutils, callbacks
from supybot.commands import *

from supybot.i18n import PluginInternationalization, internationalizeDocstring
_ = PluginInternationalization('DeepSeek')

from openai import OpenAI


class DeepSeek(callbacks.Plugin):
    """DeepSeek API implementation."""
    threaded = True
    conf.supybot.capabilities().add('-DeepSeek')

    @internationalizeDocstring
    def msg(self, irc, msg, args, text):
        """<message>"""

        client = OpenAI(api_key=self.registryValue('api_key'),
                        base_url='https://api.deepseek.com')

        prompt = self.registryValue('prompt', msg.channel).replace('$botnick',
                irc.nick)

        response = client.chat.completions.create(
            model=self.registryValue('model'),
            messages=[
                {'role': 'system', 'content': prompt},
                {'role': 'user', 'content': text},
            ],
            max_tokens=self.registryValue('max_tokens', msg.channel),
            stream=False
        )
        content = response.choices[0].message.content
        for line in content.splitlines():
            if line:
                irc.reply(line, prefixNick=False)
    msg = wrap(msg, ['text'])


Class = DeepSeek
