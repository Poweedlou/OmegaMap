from io import BytesIO
import requests
from PIL import Image


def get_bytes_image(coords, spn):
    geocoder_api_server = "http://static-maps.yandex.ru/1.x/"
    map_params = {
        "ll": ', '.join(map(str, coords)),
        "spn": spn,
        "l": "map"
    }
    response = requests.get(geocoder_api_server, params=map_params)
    return BytesIO(response.content)
