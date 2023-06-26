import requests
from data.config import connection_str as conn


def add_good(name: str, value: float):
    r = requests.post(conn+"goods/create", json={'name': name, 'value': value})
    print(r.status_code)
    if r.status_code == 200:
        return True
    return False
