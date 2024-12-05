# GisWeather

Weather plugin for [limnoria](https://limnoria.net) IRC bot. Uses [Gismeteo](https://www.gismeteo.ru/) data.

Requires [requests](https://requests.readthedocs.io) module.

## Commands

- `weather <location>` prints current weather in given location.

```
<user> @weather Moscow
<limnoria> Moscow: Mainly cloudy, 🌡️ -4.2°С (-6.6°С), 💨 1 m/s, 💧 81%, P: 765 mmHg (according to Gismeteo data)
<user> @weather Minsk
<limnoria> Minsk: Mainly cloudy, 🌡️-3.1°С (-6.2°С), 💨2 m/s, 💧81%, P: 751 mmHg (according to Gismeteo data)
```

## Configuration

- **supybot.plugins.GisWeather.token** - Gismeteo application token (required for data fetching).
    - Contact [b2b [at] gismeteo.ru](https://www.gismeteo.ru/b2b/) by e-mail to get it.

- **supybot.plugins.GisWeather.language** - language code (2 chars), which will be used in queries. See [possible values in official API documentation](https://www.gismeteo.ru/api/).
    - `"en"` by default.

- **supybot.plugins.GisWeather.template** - reply template that will be formatted with weather data.
    - `"{loc}: {desc}, 🌡️ {temp}°С ({temp_like}°С), 💨 {wind_sp} m/s, 💧 {hum}%, P: {pressure} mmHg"` by default.
