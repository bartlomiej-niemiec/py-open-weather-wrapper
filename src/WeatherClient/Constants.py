ALLOWED_OPTIONAL_PARS_WEATHER = ['units', 'lang', 'mode']
ALLOWED_OPTIONAL_PARS_FORECAST = ['units', 'lang', 'mode', 'cnt']


class Unit:
    KELVIN = None
    FAHRENHEIT = "imperial"
    CELSIUS = "metric"


class Format:
    DICT = "dict"
    JSON = 'json'
    XML = 'xml'


class Language:
    Afrikaans = 'af'
    Albanian = 'al'
    Arabic = 'ar'
    Azerbaijani = 'az'
    Bulgarian = 'bg'
    Catalan = 'ca'
    Czech = 'cz'
    Danish = 'da'
    German = 'de'
    Greek = 'el'
    English = 'en'
    Basque = 'eu'
    Persian = 'fa'
    Finnish = 'fi'
    French = 'fr'
    Galician = 'gl'
    Hebrew = 'he'
    Hindi = 'hi'
    Croatian = 'hr'
    Hungarian = 'hu'
    Indonesian = 'id'
    Italian = 'it'
    Japanese = 'ja'
    Korean = 'kr'
    Latvian = 'la'
    Lithuanian = 'lt'
    Macedonian = 'lt'
    Norwegian = 'no'
    Dutch = 'nl'
    Polish = 'pl'
    Portuguese = 'pt'
    Português = 'pt_br'
    Brasil = 'pt_br'
    Romanian = 'ro'
    Russian = 'ru'
    Swedish = 'sv'
    Slovak = 'sk'
    Slovenian = 'sl'
    Spanish = 'sp'
    Serbian = 'sr'
    Thai = 'th'
    Turkish = 'tr'
    Ukrainian = 'ua'
    Vietnamese = 'vi'
    Chinese_Simplified = 'zh_cn'
    Chinese_Traditional = 'zh_tw'
    Zulu = 'zu'
