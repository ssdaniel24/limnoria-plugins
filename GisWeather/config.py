from supybot import conf, registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('GisWeather')
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
    conf.registerPlugin('GisWeather', True)


GisWeather = conf.registerPlugin('GisWeather')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(GisWeather, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))

conf.registerGlobalValue(
    GisWeather,
    'token',
    registry.String(
        '', _("""Gismeteo application token""")
    )
)

conf.registerNetworkValue(
    GisWeather,
    'language',
    registry.String(
        'en', _("""Language code for requests""")
    )
)

conf.registerChannelValue(
    GisWeather,
    'template',
    registry.String(
        '{loc}: {desc}, 🌡️ {temp}°С ({temp_like}°С), 💨 {wind_sp} m/s, '
        '💧 {hum}%, P: {pressure} mmHg',
        _("""Template for reply with weather data""")
    )
)


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
