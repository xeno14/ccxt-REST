from flask_restplus import fields
import warnings


def get_models():
    return _models.copy()


def get_model(method: str) -> dict:
    if method not in _models:
        warnings.warn("Method '%s' is not found in models." % method)
        return {}
    return _models[method]


_models = {
    'cancelOrder': {
        'id': fields.String(required=False, description='id', example='orderid123456'),
        'symbol': fields.String(required=False, description='symbol', example='ETH/BTC'),
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'createOrder': {
        'symbol': fields.String(required=False, description='symbol', example='ETH/BTC'),
        'type': fields.String(required=False, description='type', example='limit'),
        'side': fields.String(required=False, description='side', example='buy'),
        'amount': fields.Float(required=False, description='amount', example='1'),
        'price': fields.Float(required=False, description='price', example='0.035'),
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'createLimitOrder': {
        'symbol': fields.String(required=False, description='symbol', example='ETH/BTC'),
        'args': fields.Raw(required=False, description='args', example=''),
    },
    'editOrder': {
        'id': fields.String(required=False, description='id', example='orderid123456'),
        'symbol': fields.String(required=False, description='symbol', example='ETH/BTC'),
        'args': fields.Raw(required=False, description='args', example=''),
    },
    'fetchBalance': {
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'fetchClosedOrders': {
        'symbol': fields.String(required=False, description='symbol', example='ETH/BTC'),
        'since': fields.String(required=False, description='since', example=''),
        'limit': fields.String(required=False, description='limit', example=''),
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'fetchCurrencies': {
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'fetchDepositAddress': {
        'code': fields.String(required=False, description='code', example=''),
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'fetchL2OrderBook': {
        'symbol': fields.String(required=False, description='symbol', example='ETH/BTC'),
        'limit': fields.String(required=False, description='limit', example=''),
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'fetchMarkets': {
    },
    'fetchOHLCV': {
        'symbol': fields.String(required=False, description='symbol', example='ETH/BTC'),
        'timeframe': fields.String(required=False, description='timeframe', example=''),
        'since': fields.String(required=False, description='since', example=''),
        'limit': fields.String(required=False, description='limit', example=''),
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'fetchOpenOrders': {
        'symbol': fields.String(required=False, description='symbol', example='ETH/BTC'),
        'since': fields.String(required=False, description='since', example=''),
        'limit': fields.String(required=False, description='limit', example=''),
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'fetchOrder': {
        'id': fields.String(required=False, description='id', example='orderid123456'),
        'symbol': fields.String(required=False, description='symbol', example='ETH/BTC'),
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'fetchOrderBook': {
        'symbol': fields.String(required=False, description='symbol', example='ETH/BTC'),
        'limit': fields.String(required=False, description='limit', example=''),
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'fetchTicker': {
        'symbol': fields.String(required=False, description='symbol', example='ETH/BTC'),
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'fetchTickers': {
        'symbols': fields.String(required=False, description='symbols', example=''),
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'fetchTrades': {
        'symbol': fields.String(required=False, description='symbol', example='ETH/BTC'),
        'since': fields.String(required=False, description='since', example=''),
        'limit': fields.String(required=False, description='limit', example=''),
        'params': fields.Raw(required=False, description='params', example=''),
    },
    'withdraw': {
        'code': fields.String(required=False, description='code', example=''),
        'amount': fields.Float(required=False, description='amount', example='1'),
        'address': fields.String(required=False, description='address', example=''),
        'tag': fields.String(required=False, description='tag', example=''),
        'params': fields.Raw(required=False, description='params', example=''),
    },
}
