import requests
import json

api_request = requests.get(
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=94b6c234-f483-4cfe-83f2-06eddf1002aa"
)
api = json.loads(api_request.content)

coins = [{
    "symbol":"BTC",
    "amount_owned" : 2,
    "price_per_coin":3200
},
    {
    "symbol":"ETH",
    "amount_owned" : 100,
    "price_per_coin":2.50
}]
for i in range(0, 4):
    for coin in coins:
        if api["data"][i]["symbol"] == coin["symbol"]:

            print( api["data"][i]["symbol"] + "---" + api["data"][i]["symbol"])
            print("{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("--------------------*------------------------------")