from django.shortcuts import render
import requests


symbols = ['BTC','ETH','XRP','LTC']

# Returns tuple(Symbol, Delta)
def toDelta(symbol):
    params = {"fsym": symbol, "tsym": "USD", "e": "CCCAGG"}
    r = requests.get('https://min-api.cryptocompare.com/data/generateAvg', params=params)
    return (symbol, r.json()["RAW"]["CHANGEPCT24HOUR"])


def index(request):
    deltas = map(toDelta, symbols)
    lowest = sorted(deltas, key=lambda x:x[1])[0]
    return render(request, 'index.html', {'crashing': lowest[0], 'delta': lowest[1]})
