from ccxtrest.apis import api
from ccxtrest._core.models import get_model
from ccxtrest._core.exchange import get_exchange

from flask import Flask, request
from flask_restplus import Resource, Api, fields


namespace = api.namespace("poloniex", description="poloniex")
api.add_namespace(namespace)


model_cancelOrder = namespace.model("cancelOrder", get_model("cancelOrder"))
model_createDepositAddress = namespace.model("createDepositAddress", get_model("createDepositAddress"))
model_createOrder = namespace.model("createOrder", get_model("createOrder"))
model_createLimitOrder = namespace.model("createLimitOrder", get_model("createLimitOrder"))
model_editOrder = namespace.model("editOrder", get_model("editOrder"))
model_fetchBalance = namespace.model("fetchBalance", get_model("fetchBalance"))
model_fetchClosedOrders = namespace.model("fetchClosedOrders", get_model("fetchClosedOrders"))
model_fetchCurrencies = namespace.model("fetchCurrencies", get_model("fetchCurrencies"))
model_fetchDepositAddress = namespace.model("fetchDepositAddress", get_model("fetchDepositAddress"))
model_fetchL2OrderBook = namespace.model("fetchL2OrderBook", get_model("fetchL2OrderBook"))
model_fetchMarkets = namespace.model("fetchMarkets", get_model("fetchMarkets"))
model_fetchMyTrades = namespace.model("fetchMyTrades", get_model("fetchMyTrades"))
model_fetchOHLCV = namespace.model("fetchOHLCV", get_model("fetchOHLCV"))
model_fetchOpenOrders = namespace.model("fetchOpenOrders", get_model("fetchOpenOrders"))
model_fetchOrder = namespace.model("fetchOrder", get_model("fetchOrder"))
model_fetchOrderBook = namespace.model("fetchOrderBook", get_model("fetchOrderBook"))
model_fetchOrders = namespace.model("fetchOrders", get_model("fetchOrders"))
model_fetchTicker = namespace.model("fetchTicker", get_model("fetchTicker"))
model_fetchTickers = namespace.model("fetchTickers", get_model("fetchTickers"))
model_fetchTrades = namespace.model("fetchTrades", get_model("fetchTrades"))
model_fetchTradingFees = namespace.model("fetchTradingFees", get_model("fetchTradingFees"))
model_withdraw = namespace.model("withdraw", get_model("withdraw"))
model_fetchOrderTrades = namespace.model("fetchOrderTrades", get_model("fetchOrderTrades"))


@namespace.route("/cancelOrder", methods=["post"])
class cancelOrder(Resource):

     @namespace.expect(model_cancelOrder)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.cancelOrder(**data)
        return result


@namespace.route("/createDepositAddress", methods=["post"])
class createDepositAddress(Resource):

     @namespace.expect(model_createDepositAddress)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.createDepositAddress(**data)
        return result


@namespace.route("/createOrder", methods=["post"])
class createOrder(Resource):

     @namespace.expect(model_createOrder)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.createOrder(**data)
        return result


@namespace.route("/createLimitOrder", methods=["post"])
class createLimitOrder(Resource):

     @namespace.expect(model_createLimitOrder)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.createLimitOrder(**data)
        return result


@namespace.route("/editOrder", methods=["post"])
class editOrder(Resource):

     @namespace.expect(model_editOrder)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.editOrder(**data)
        return result


@namespace.route("/fetchBalance", methods=["post"])
class fetchBalance(Resource):

     @namespace.expect(model_fetchBalance)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchBalance(**data)
        return result


@namespace.route("/fetchClosedOrders", methods=["post"])
class fetchClosedOrders(Resource):

     @namespace.expect(model_fetchClosedOrders)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchClosedOrders(**data)
        return result


@namespace.route("/fetchCurrencies", methods=["post"])
class fetchCurrencies(Resource):

     @namespace.expect(model_fetchCurrencies)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchCurrencies(**data)
        return result


@namespace.route("/fetchDepositAddress", methods=["post"])
class fetchDepositAddress(Resource):

     @namespace.expect(model_fetchDepositAddress)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchDepositAddress(**data)
        return result


@namespace.route("/fetchL2OrderBook", methods=["post"])
class fetchL2OrderBook(Resource):

     @namespace.expect(model_fetchL2OrderBook)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchL2OrderBook(**data)
        return result


@namespace.route("/fetchMarkets", methods=["post"])
class fetchMarkets(Resource):

     @namespace.expect(model_fetchMarkets)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchMarkets(**data)
        return result


@namespace.route("/fetchMyTrades", methods=["post"])
class fetchMyTrades(Resource):

     @namespace.expect(model_fetchMyTrades)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchMyTrades(**data)
        return result


@namespace.route("/fetchOHLCV", methods=["post"])
class fetchOHLCV(Resource):

     @namespace.expect(model_fetchOHLCV)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchOHLCV(**data)
        return result


@namespace.route("/fetchOpenOrders", methods=["post"])
class fetchOpenOrders(Resource):

     @namespace.expect(model_fetchOpenOrders)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchOpenOrders(**data)
        return result


@namespace.route("/fetchOrder", methods=["post"])
class fetchOrder(Resource):

     @namespace.expect(model_fetchOrder)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchOrder(**data)
        return result


@namespace.route("/fetchOrderBook", methods=["post"])
class fetchOrderBook(Resource):

     @namespace.expect(model_fetchOrderBook)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchOrderBook(**data)
        return result


@namespace.route("/fetchOrders", methods=["post"])
class fetchOrders(Resource):

     @namespace.expect(model_fetchOrders)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchOrders(**data)
        return result


@namespace.route("/fetchTicker", methods=["post"])
class fetchTicker(Resource):

     @namespace.expect(model_fetchTicker)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchTicker(**data)
        return result


@namespace.route("/fetchTickers", methods=["post"])
class fetchTickers(Resource):

     @namespace.expect(model_fetchTickers)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchTickers(**data)
        return result


@namespace.route("/fetchTrades", methods=["post"])
class fetchTrades(Resource):

     @namespace.expect(model_fetchTrades)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchTrades(**data)
        return result


@namespace.route("/fetchTradingFees", methods=["post"])
class fetchTradingFees(Resource):

     @namespace.expect(model_fetchTradingFees)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchTradingFees(**data)
        return result


@namespace.route("/withdraw", methods=["post"])
class withdraw(Resource):

     @namespace.expect(model_withdraw)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.withdraw(**data)
        return result


@namespace.route("/fetchOrderTrades", methods=["post"])
class fetchOrderTrades(Resource):

     @namespace.expect(model_fetchOrderTrades)
     def post(self):
        exchange = get_exchange("poloniex")
        data = request.json
        result = exchange.fetchOrderTrades(**data)
        return result
