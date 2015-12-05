import requests

MADLIBS_URL = 'https://murmuring-depths-4074.herokuapp.com'


def get_template(id=None):
    if id is not None:
        url = MADLIBS_URL + '/template/' + str(id)
    else:
        url = MADLIBS_URL + '/template'
    result = requests.get(url)
    return result.json()


def post_madlib(madlib):
    url = MADLIBS_URL + '/madlib'
    result = requests.post(url, json=madlib)
    return result.json()


if __name__ == '__main__':
    t = get_template()
    print(str(t))
    t = get_template(1)
    print(str(t))
    m = {'title': 'Merry Xmas', 'content': 'this is a madlib, can\'t you tell?', 'author': 'me'}
    post_madlib(m)
