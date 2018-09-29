from ccxtrest.apis import api
from flask import Flask
from ccxtrest.apis import bitflyer, bittrex, poloniex


app = Flask(__name__)


def init():
    api.init_app(app)


if __name__ == '__main__':
    init()
    app.run(debug=True)

