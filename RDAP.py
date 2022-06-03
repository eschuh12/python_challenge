import requests
import json


def rdapLookup_b(ip):
    url = f'https://rdap.arin.net/registry/ip/{ip}'
    x = requests.get(url, headers={'accept': 'application/json'})
    y = x.json()
    print(y["handle"])
    print(y["startAddress"])
    print(y["endAddress"])
    print(y["ipVersion"])
    print(y["name"])
    print(y["type"])
    print(y["parentHandle"])


def rdapLookup_d(ip):
    url = f'https://rdap.arin.net/registry/ip/{ip}'
    x = requests.get(url, headers={'accept': 'application/json'})
    y = json.loads(x.text)
    print(json.dumps(y, indent=2))


