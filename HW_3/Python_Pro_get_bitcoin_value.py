from http import HTTPStatus
from webargs import validate

import httpx
from flask import Flask, Response, jsonify
from webargs import fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)

@app.route("/get-bitcoin-value")
@use_kwargs(
    {
        "currency": fields.Str(
            missing='USD'.upper(),
            validate=validate.Length(min=2, max=10),
            error_messages={
                "required": "Currency code is required",
                "length": "Currency code must be between 2 and 10 characters long"
            }
        ),
        "convert": fields.Int(
            missing=1,
            validate=validate.Range(min=1, max=1000),
            error_messages={
                "invalid": "Number must be a valid integer",
                "validator_failed": "Number must be between 1 and 1000"
            }
        )
    },
    location="query"
)

def get_bitcoin_value(currency, convert):
    url = "https://bitpay.com/api/rates"
    result = httpx.get(url=url, params={})
    if result.status_code not in (HTTPStatus.OK,):
        return Response("ERROR: Something went wrong with api.open-notify.org!",
                        status=result.status_code)
    result = result.json()
    currency_rate = next((rate for rate in result if rate['code'] == currency), None)
    if currency_rate is None:
        return jsonify({"error": "Currency code not found"}), HTTPStatus.NOT_FOUND
    rate = currency_rate['rate']
    total_value = rate * convert
    return jsonify({
        "currency": currency,
        "rate": rate,
        "convert": convert,
        "total_value": total_value
    })


if __name__ == '__main__':
    app.run(debug=True, port=5002)

