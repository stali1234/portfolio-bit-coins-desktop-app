import requests
import json

api_request = requests.get(
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=94b6c234-f483-4cfe-83f2-06eddf1002aa"
)
api = json.loads(api_request.content)

total_price = 0
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
            total_paid = coin["amount_owned"] * coin["price_per_coin"]
            current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
            pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
            total_pl_coin = pl_percoin*coin["amount_owned"]
            total_price = total_price + total_pl_coin
            print("price -${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("number of coins" , coin["amount_owned"])
            print("total amount of paid","${0:.2f}".format(total_paid))
            print("current value","${0:.2f}".format(current_value))
            print("p/l per coin" , "${0:.2f}".format(pl_percoin))
            print("total p/l with coin:","${0:.2f}".format(total_pl_coin))
            
            print("--------------------*------------------------------")

print("total p/l for portfolio","${0:.2f}".format(total_price))            