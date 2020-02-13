import requests
import lxml.etree


geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "format": "xml"}


def scale(site):
    geocoder_params['geocode'] = site
    response = requests.get(geocoder_api_server, params=geocoder_params)
    root = lxml.etree.fromstring(response.content)
    lx, ly = list(map(float, root.findtext('.//{*}lowerCorner').split()))
    ux, uy = list(map(float, root.findtext('.//{*}upperCorner').split()))
    dx, dy = abs(lx - ux), abs(ly - uy)
    d = max((dx, dy)) / 2
    coords = tuple(map(float, root.findtext('.//{*}pos').split()))
    return list(coords), d