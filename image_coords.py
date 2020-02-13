from io import BytesIO
import requests


def get_bytes_image(coords, spn):
    string = [str(elem) for elem in coords]
    x = string[0]
    if '.' not in x:
        x = f'{x}.000000'
    else:
        p = x.split('.')
        if len(list(p[1])) < 6:
            right = p[1].ljust(6, '0')
        x = f'{p[0]}.{right}'
    y = string[1]
    if '.' not in y:
        y = f'{y}.000000'
    else:
        p = y.split('.')
        if len(list(p[1])) < 6:
            right = p[1].ljust(6, '0')
        y = f'{p[0]}.{right}'
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    map_params = {
        "ll": ','.join([x, y]),
        "spn": spn,
        "l": "map"
    }
    response = requests.get(map_api_server, params=map_params)
    if not response:
        with open('err.xml', 'wb') as fo:
            fo.write(response.content)
        print(map_params['ll'])
    return BytesIO(response.content)
