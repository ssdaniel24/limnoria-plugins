from supybot import conf, registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('DeepSeek')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified themself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('DeepSeek', True)


DeepSeek = conf.registerPlugin('DeepSeek')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(DeepSeek, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))
conf.registerGlobalValue(DeepSeek, 'api_key',
        registry.String('', _("""Your DeepSeek API Key (required)"""),
        private=True))

conf.registerChannelValue(DeepSeek, 'prompt',
        registry.String(
            """Ты $botnick - IRC-бот. Будь вежлив и помогай пользователю.""",
            _("""Prompt that configures AI""")
        ))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
