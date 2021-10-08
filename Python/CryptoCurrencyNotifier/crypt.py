import notify2
import requests
from cryptocompy import price
def fetch_coin(coin,fiat):
    r=price.get_current_price(coin,fiat)
    return r[coin][fiat]

def notify():
    icon_path="/home/aakarsh/Desktop/Desktop Notification/logo.jpg"
    cryptocurrencies=["BTC","ETH","LTC","XMR","XRP",]
    result="\n"
    for coin in cryptocurrencies:
        rate=fetch_coin(coin,"USD")
        result+="{}-{}\n".format(coin,"$"+str(rate))

    notify2.init("Cryptocurrency rates notifier")
    n=notify2.Notification("Crypto Notifier",icon=icon_path)
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(1000)
    n.update("Current Cryptocurrency Rates",result)
    n.show()

if __name__ == "__main__":
    notify()
