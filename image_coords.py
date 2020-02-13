from io import BytesIO
import requests


def get_bytes_image(coords, spn):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    map_params = {
        "ll": ','.join(map(str, coords)),
        "spn": spn,
        "l": "map"
    }
    response = requests.get(map_api_server, params=map_params)
    if not response: 
        with open('err.xml', 'wb') as fo:
            fo.write(response.content)
        print(map_params['ll'])
    return BytesIO(response.content)
