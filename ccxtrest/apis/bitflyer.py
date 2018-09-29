from ccxtrest.apis import api
from ccxtrest._core.models import get_model
from ccxtrest._core.exchange import get_exchange

from flask import Flask, request
from flask_restplus import Resource, Api, fields


namespace = api.namespace("bitflyer", description="bitflyer")
api.add_namespace(namespace)


model_cancelOrder = namespace.model("cancelOrder", get_model("cancelOrder"))
model_createOrder = namespace.model("createOrder", get_model("createOrder"))
model_createMarketOrder = namespace.model("createMarketOrder", get_model("createMarketOrder"))
model_createLimitOrder = namespace.model("createLimitOrder", get_model("createLimitOrder"))
model_editOrder = namespace.model("editOrder", get_model("editOrder"))
model_fetchBalance = namespace.model("fetchBalance", get_model("fetchBalance"))
model_fetchClosedOrders = namespace.model("fetchClosedOrders", get_model("fetchClosedOrders"))
model_fetchL2OrderBook = namespace.model("fetchL2OrderBook", get_model("fetchL2OrderBook"))
model_fetchMarkets = namespace.model("fetchMarkets", get_model("fetchMarkets"))
model_fetchMyTrades = namespace.model("fetchMyTrades", get_model("fetchMyTrades"))
model_fetchOHLCV = namespace.model("fetchOHLCV", get_model("fetchOHLCV"))
model_fetchOpenOrders = namespace.model("fetchOpenOrders", get_model("fetchOpenOrders"))
model_fetchOrder = namespace.model("fetchOrder", get_model("fetchOrder"))
model_fetchOrderBook = namespace.model("fetchOrderBook", get_model("fetchOrderBook"))
model_fetchOrders = namespace.model("fetchOrders", get_model("fetchOrders"))
model_fetchTicker = namespace.model("fetchTicker", get_model("fetchTicker"))
model_fetchTrades = namespace.model("fetchTrades", get_model("fetchTrades"))
model_withdraw = namespace.model("withdraw", get_model("withdraw"))


@namespace.route("/cancelOrder", methods=["post"])
class cancelOrder(Resource):

     @namespace.expect(model_cancelOrder)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.cancelOrder(**data)
        return result


@namespace.route("/createOrder", methods=["post"])
class createOrder(Resource):

     @namespace.expect(model_createOrder)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.createOrder(**data)
        return result


@namespace.route("/createMarketOrder", methods=["post"])
class createMarketOrder(Resource):

     @namespace.expect(model_createMarketOrder)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.createMarketOrder(**data)
        return result


@namespace.route("/createLimitOrder", methods=["post"])
class createLimitOrder(Resource):

     @namespace.expect(model_createLimitOrder)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.createLimitOrder(**data)
        return result


@namespace.route("/editOrder", methods=["post"])
class editOrder(Resource):

     @namespace.expect(model_editOrder)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.editOrder(**data)
        return result


@namespace.route("/fetchBalance", methods=["post"])
class fetchBalance(Resource):

     @namespace.expect(model_fetchBalance)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.fetchBalance(**data)
        return result


@namespace.route("/fetchClosedOrders", methods=["post"])
class fetchClosedOrders(Resource):

     @namespace.expect(model_fetchClosedOrders)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.fetchClosedOrders(**data)
        return result


@namespace.route("/fetchL2OrderBook", methods=["post"])
class fetchL2OrderBook(Resource):

     @namespace.expect(model_fetchL2OrderBook)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.fetchL2OrderBook(**data)
        return result


@namespace.route("/fetchMarkets", methods=["post"])
class fetchMarkets(Resource):

     @namespace.expect(model_fetchMarkets)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.fetchMarkets(**data)
        return result


@namespace.route("/fetchMyTrades", methods=["post"])
class fetchMyTrades(Resource):

     @namespace.expect(model_fetchMyTrades)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.fetchMyTrades(**data)
        return result


@namespace.route("/fetchOHLCV", methods=["post"])
class fetchOHLCV(Resource):

     @namespace.expect(model_fetchOHLCV)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.fetchOHLCV(**data)
        return result


@namespace.route("/fetchOpenOrders", methods=["post"])
class fetchOpenOrders(Resource):

     @namespace.expect(model_fetchOpenOrders)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.fetchOpenOrders(**data)
        return result


@namespace.route("/fetchOrder", methods=["post"])
class fetchOrder(Resource):

     @namespace.expect(model_fetchOrder)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.fetchOrder(**data)
        return result


@namespace.route("/fetchOrderBook", methods=["post"])
class fetchOrderBook(Resource):

     @namespace.expect(model_fetchOrderBook)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.fetchOrderBook(**data)
        return result


@namespace.route("/fetchOrders", methods=["post"])
class fetchOrders(Resource):

     @namespace.expect(model_fetchOrders)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.fetchOrders(**data)
        return result


@namespace.route("/fetchTicker", methods=["post"])
class fetchTicker(Resource):

     @namespace.expect(model_fetchTicker)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.fetchTicker(**data)
        return result


@namespace.route("/fetchTrades", methods=["post"])
class fetchTrades(Resource):

     @namespace.expect(model_fetchTrades)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.fetchTrades(**data)
        return result


@namespace.route("/withdraw", methods=["post"])
class withdraw(Resource):

     @namespace.expect(model_withdraw)
     def post(self):
        exchange = get_exchange("bitflyer")
        data = request.json
        result = exchange.withdraw(**data)
        return result
