import requests
import json
from tkinter import *

pycrypto = Tk()
pycrypto.title("MY crypto portfolio")


def my_protfolio():
    api_request = requests.get(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=94b6c234-f483-4cfe-83f2-06eddf1002aa"
    )
    api = json.loads(api_request.content)

    total_price = 0
    coins = [
        {"symbol": "BTC", "amount_owned": 2, "price_per_coin": 3200},
        {"symbol": "ETH", "amount_owned": 100, "price_per_coin": 2.50},
    ]
    for i in range(0, 4):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                total_paid = coin["amount_owned"] * coin["price_per_coin"]
                current_value = (
                    coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
                )
                pl_percoin = (
                    api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                )
                total_pl_coin = pl_percoin * coin["amount_owned"]
                total_price = total_price + total_pl_coin
                print("price -${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                print("number of coins", coin["amount_owned"])
                print("total amount of paid", "${0:.2f}".format(total_paid))
                print("current value", "${0:.2f}".format(current_value))
                print("p/l per coin", "${0:.2f}".format(pl_percoin))
                print("total p/l with coin:", "${0:.2f}".format(total_pl_coin))

                print("--------------------*------------------------------")


# print("total p/l for portfolio", "${0:.2f}".format(total_price))
name = Label(pycrypto, text="Coin name", bg="black", fg="white")
name.grid(row=0, column=0, sticky=N + S + E + W)
name = Label(pycrypto, text="Price", bg="black", fg="white")
name.grid(row=0, column=1, sticky=N + S + E + W)
name = Label(pycrypto, text="Coin Owned", bg="black", fg="white")
name.grid(row=0, column=2, sticky=N + S + E + W)
name = Label(pycrypto, text="Total Amount Paid", bg="black", fg="white")
name.grid(row=0, column=3, sticky=N + S + E + W)
name = Label(pycrypto, text="Current Value", bg="black", fg="white")
name.grid(row=0, column=4, sticky=N + S + E + W)
name = Label(pycrypto, text="p/l per coin", bg="black", fg="white")
name.grid(row=0, column=5, sticky=N + S + E + W)
name = Label(pycrypto, text="Total p/l with coin", bg="black", fg="white")
name.grid(row=0, column=6, sticky=N + S + E + W)

pycrypto.mainloop()