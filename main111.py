import requests
import json
from tkinter import *
import sqlite3

pycrypto = Tk()
pycrypto.title("MY crypto portfolio")

con = sqlite3.connect("coin.db")
cobj = con.cursor()

# cobj.execute("INSERT INTO coin VALUES(1,'BTC',2,3250)")
# con.commit()
# cobj.execute("INSERT INTO coin VALUES(2,'ETH',3,240)")
# con.commit()
# cobj.execute("INSERT INTO coin VALUES(3,'USDT',6,32550)")
# con.commit()

# cobj.execute("INSERT INTO coin VALUES(4,'DOT',2,34550)")
# con.commit()
# cobj.execute("DELETE FROM coin")
# con.commit()


def font_color(amount):
    if amount > 0:
        return "green"
    else:
        return "red"


def my_protfolio():
    api_request = requests.get(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=94b6c234-f483-4cfe-83f2-06eddf1002aa"
    )
    api = json.loads(api_request.content)

    total_price = 0
    coin_row = 1
    total_current_value = 0
    cobj.execute("SELECT * FROM coin")
    coins = cobj.fetchall()
    for i in range(0, 5):
        for coin in coins:
            if api["data"][i]["symbol"] == coin[1]:
                total_paid = coin[2] * coin[3]
                current_value = coin[2] * api["data"][i]["quote"]["USD"]["price"]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin[3]
                total_pl_coin = pl_percoin * coin[2]
                total_price = total_price + total_pl_coin
                total_current_value = total_current_value + current_value

                name = Label(
                    pycrypto,
                    text=api["data"][i]["symbol"],
                    bg="grey",
                    fg="black",
                    font="Lato 12 bold",
                    padx="5",
                    pady="5",
                    borderwidth=2,
                    relief="groove",
                )
                name.grid(row=coin_row, column=0, sticky=N + S + E + W)
                price = Label(
                    pycrypto,
                    text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]),
                    bg="grey",
                    fg="black",
                    font="Lato 12 bold",
                    padx="5",
                    pady="5",
                    borderwidth=2,
                    relief="groove",
                )
                price.grid(row=coin_row, column=1, sticky=N + S + E + W)
                no_coins = Label(
                    pycrypto,
                    text=coin[2],
                    bg="grey",
                    fg="black",
                    font="Lato 12 bold",
                    padx="5",
                    pady="5",
                    borderwidth=2,
                    relief="groove",
                )
                no_coins.grid(row=coin_row, column=2, sticky=N + S + E + W)
                amount_paid = Label(
                    pycrypto,
                    text="${0:.2f}".format(total_paid),
                    bg="grey",
                    fg="black",
                    font="Lato 12 bold",
                    padx="5",
                    pady="5",
                    borderwidth=2,
                    relief="groove",
                )
                amount_paid.grid(row=coin_row, column=3, sticky=N + S + E + W)
                current_val = Label(
                    pycrypto,
                    text="${0:.2f}".format(current_value),
                    bg="grey",
                    fg=font_color(float("{0:.2f}".format(current_value))),
                    font="Lato 12 bold",
                    padx="5",
                    pady="5",
                    borderwidth=2,
                    relief="groove",
                )
                current_val.grid(row=coin_row, column=4, sticky=N + S + E + W)
                pl_coin = Label(
                    pycrypto,
                    text="${0:.2f}".format(pl_percoin),
                    bg="grey",
                    fg="black",
                    font="Lato 12 bold",
                    padx="5",
                    pady="5",
                    borderwidth=2,
                    relief="groove",
                )
                pl_coin.grid(row=coin_row, column=5, sticky=N + S + E + W)
                totalpl = Label(
                    pycrypto,
                    text="${0:.2f}".format(total_pl_coin),
                    bg="grey",
                    fg="black",
                    font="Lato 12 bold",
                    padx="5",
                    pady="5",
                    borderwidth=2,
                    relief="groove",
                )
                totalpl.grid(row=coin_row, column=6, sticky=N + S + E + W)
                coin_row = coin_row + 1
            totalpl = Label(
                pycrypto,
                text="${0:.2f}".format(total_price),
                bg="grey",
                fg="black",
                font="Lato 12 bold",
                padx="5",
                pady="5",
                borderwidth=2,
                relief="groove",
            )
            totalpl.grid(row=6, column=6, sticky=N + S + E + W)
            totalpll = Label(
                pycrypto,
                text="${0:.2f}".format(total_current_value),
                bg="grey",
                fg="black",
                font="Lato 12 bold",
                padx="5",
                pady="5",
                borderwidth=2,
                relief="groove",
            )

            totalplll = Button(
                pycrypto,
                text="update",
                bg="grey",
                fg="black",
                font="Lato 12 bold",
                command=my_protfolio,
                padx="5",
                pady="5",
                borderwidth=2,
                relief="groove",
            )
            totalplll.grid(row=7, column=6, sticky=N + S + E + W)


# print("total p/l for portfolio", "${0:.2f}".format(total_price))
def application_header():
    name = Label(
        pycrypto,
        text="Coin name",
        bg="#142E54",
        fg="white",
        font="Lato 12 bold",
        padx="5",
        pady="5",
        borderwidth=2,
        relief="groove",
    )
    name.grid(row=0, column=0, sticky=N + S + E + W)
    name = Label(
        pycrypto,
        text="Price",
        bg="#142E54",
        fg="white",
        font="Lato 12 bold",
        padx="5",
        pady="5",
        borderwidth=2,
        relief="groove",
    )
    name.grid(row=0, column=1, sticky=N + S + E + W)
    name = Label(
        pycrypto,
        text="Coin Owned",
        bg="#142E54",
        fg="white",
        font="Lato 12 bold",
        padx="5",
        pady="5",
        borderwidth=2,
        relief="groove",
    )
    name.grid(row=0, column=2, sticky=N + S + E + W)
    name = Label(
        pycrypto,
        text="Total Amount Paid",
        bg="#142E54",
        fg="white",
        font="Lato 12 bold",
        padx="5",
        pady="5",
        borderwidth=2,
        relief="groove",
    )
    name.grid(row=0, column=3, sticky=N + S + E + W)
    name = Label(
        pycrypto,
        text="Current Value",
        bg="#142E54",
        fg="white",
        font="Lato 12 bold",
        padx="5",
        pady="5",
        borderwidth=2,
        relief="groove",
    )
    name.grid(row=0, column=4, sticky=N + S + E + W)
    name = Label(
        pycrypto,
        text="p/l per coin",
        bg="#142E54",
        fg="white",
        font="Lato 12 bold",
        padx="5",
        pady="5",
        borderwidth=2,
        relief="groove",
    )
    name.grid(row=0, column=5, sticky=N + S + E + W)
    name = Label(
        pycrypto,
        text="Total p/l with coin",
        bg="#142E54",
        fg="white",
        font="Lato 12 bold",
        padx="5",
        pady="5",
        borderwidth=2,
        relief="groove",
    )
    name.grid(row=0, column=6, sticky=N + S + E + W)


application_header()
my_protfolio()
pycrypto.mainloop()

cobj.close()
con.close()