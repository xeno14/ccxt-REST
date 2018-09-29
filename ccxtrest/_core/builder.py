import ccxt
from inspect import signature
from jinja2 import Template, Environment, FileSystemLoader


def get_signatures(exchange: ccxt.Exchange):
    """Get method signatures from an exchange

    :param exchange:
    :return: dictionary method -> signature
    """
    methods = [method for method, has in exchange.has.items() if has and hasattr(exchange, method)]
    return {method: signature(getattr(exchange, method)) for method in methods}


def signature_to_model_text(method, signature):
    print("    '%s': {" % method)
    for param, prop in signature.parameters.items():
        # type
        if param in ["params", "args"]:
            fieldType = "Raw"
        elif param in ["amount", "price"]:
            fieldType = "Float"
        else:
            fieldType = "String"

        example = {
            "id":       "orderid123456",
            "symbol":   "ETH/BTC",
            "type":     "limit",
            "side":     "buy",
            "amount":   1,
            "price":    0.035,
        }.get(param, "")
        print("        '{}': fields.{}(required=False, description='{}', example='{}'),".format(param, fieldType, param, example))
    print("    },")


def generate_api(exchange: ccxt.Exchange):
    name = exchange.__class__.__name__
    sigs = get_signatures(exchange)
    methods = list(sigs.keys())

    env = Environment(loader=FileSystemLoader("../apis"))
    template = env.get_template("api.py.jinja2")

    text = template.render({"exchange_name": name, "methods": methods})

    filename = "../apis/{}.py".format(name)
    with open(filename, "w") as f:
        f.write(text)

    print("Generated '{}'".format(filename))


if __name__ == '__main__':
    generate_api(ccxt.bittrex())
    generate_api(ccxt.poloniex())
    generate_api(ccxt.bitflyer())

    sigs = get_signatures(ccxt.bittrex())
    for method, sig in sigs.items():
        signature_to_model_text(method, sig)
