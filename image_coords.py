from io import BytesIO
import requests
from pprint import pprint


def get_bytes_image(coords, spn, mode, dot):
    spn = str(spn)
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
    if '.' not in spn:
        spn = f'{spn}.00'
    else:
        _, foo = spn.split('.')
        if len(foo) < 2:
            foo = foo.ljust(2, '0')
        spn = _ + '.' + foo
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    map_params = {
        "ll": ','.join([x, y]),
        "spn": f'{spn},{spn}',
        "l": mode,
        'size': '650,450'
    }
    if dot is not None:
        map_params['pt'] = ','.join(map(str, dot)) + ',pm2rdm'
    response = requests.get(map_api_server, params=map_params)
    if not response:
        with open('err.xml', 'wb') as fo:
            fo.write(response.content)
        pprint(map_params)
        return None
    return response.content
