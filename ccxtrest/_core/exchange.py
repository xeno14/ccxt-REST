import ccxt


_exchanges = {
    "bittrex": ccxt.bittrex(),
    "poloniex": ccxt.poloniex(),
    "bitflyer": ccxt.bitflyer(),
}


def get_exchange(name: str):
    if name not in _exchanges:
        raise RuntimeError("Exchange {} not found".format(name))
    return _exchanges[name]
