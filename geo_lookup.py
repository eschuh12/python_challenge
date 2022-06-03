import requests


def geoLookup(ip):
    url = f'http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
    x = requests.get(url, headers={'accept': 'application/json'})
    y = x.json()
    if (y["status"]) == "fail":
        print("IP status is fail")
    else:
        print(y["country"])
        print(y["regionName"])
        print(y["city"])
        print(y["timezone"])
        print(y["isp"])
