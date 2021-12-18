import requests


def parse(url):
    r = requests.get(url)
    if r.status_code == 200:
        print(r.text)
    else:
        print(f'Упс, произошла ошибка!.. \nКод ошибки - {r.status_code}', sep='\n')


url = input()
parse(url)
