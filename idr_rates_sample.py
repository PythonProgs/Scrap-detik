import requests

#json_data = requests.get('https://www.floatrates.com/daily/idr.json')
json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.9631829764996e-5,"date":"Sun, 6 Mar 2022 23:55:01 GMT","inverseRate":14361.248345404},"eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":6.3114007892174e-5,"date":"Sun, 6 Mar 2022 23:55:01 GMT","inverseRate":15844.343171938}}

for data in json_data.values():
    print(data ['code'])
    print(data ['name'])
    print(data ['date'])
    print(data ['inverseRate'])