import requests
import json


def rdapLookup_b(ip):
    url = f'https://rdap.arin.net/registry/ip/{ip}'
    x = requests.get(url, headers={'accept': 'application/json'})
    y = x.json()
    try:
        print(y["handle"])
    except KeyError:
        print("Handle not available")
    print(y["startAddress"])
    print(y["endAddress"])
    print(y["ipVersion"])
    try:
        print(y["name"])
    except KeyError:
        print("name not available")
    try:
        print(y["type"])
    except KeyError:
        print("type not available")
    try:
        print(y["parentHandle"])
    except KeyError:
        print("parentHandle not available")



def rdapLookup_d(ip):
    url = f'https://rdap.arin.net/registry/ip/{ip}'
    x = requests.get(url, headers={'accept': 'application/json'})
    y = json.loads(x.text)
    print(json.dumps(y, indent=2))
