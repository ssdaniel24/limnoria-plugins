from supybot import conf, registry


def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified themself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('RateCBR', True)


RateCBR = conf.registerPlugin('RateCBR')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(RateCBR, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))

conf.registerChannelValue(
    RateCBR,
    'template',
    registry.String(
        '{code}: {nominal} {name} = {value} руб',
        """Формат вывода курса валюты""",
    )
)

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
