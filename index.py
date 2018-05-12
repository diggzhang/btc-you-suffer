# -*- coding: utf-8 -*-
import os
import requests
import time
import subprocess


def sound_quick(sound_file):
    sfile = os.getcwd() + '/' + sound_file
    subprocess.Popen(['mpg321', '-q', sfile]).wait()


def moniter(high, low):

    currency = 'CNY'
    url = 'https://blockchain.info/ticker'
    last_sent = 0

    while True:
        try:
            data = requests.get(url).json()
        except:
            time.sleep(3)
            continue

        price = float(data[currency]['last'])
        buy = str(data[currency]['buy'])
        sell = str(data[currency]['sell'])
        symbol = str(data[currency]['symbol'])

        if price > high or price < low:
            print(price)
            sound_quick("u_s.mp3")

        print("Price: " + symbol + str(price) + " Buy: " + symbol + buy +
              "  Sell: " + symbol + sell)
        time.sleep(3)


if __name__ == "__main__":
    high = 420
    low = 400
    moniter(high, low)
