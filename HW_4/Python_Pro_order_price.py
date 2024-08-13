from flask import Flask, jsonify
from webargs import fields as webargs_fields
from webargs.flaskparser import use_kwargs
from database_handler import execute_query

app = Flask(__name__)


@app.route("/order-price")
@use_kwargs(
    {
        "country": webargs_fields.Str(missing=None),
    },
    location="query"
)
def order_price(country):
    query = """
    SELECT invoices.InvoiceId, 
           SUM(invoice_items.UnitPrice * invoice_items.Quantity) AS Sales, 
           invoices.BillingCountry 
    FROM invoices
    JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
    """

    fields = {}
    if country:
        fields['invoices.BillingCountry'] = country

    if fields:
        query += " WHERE " + " AND ".join(
            f"{key} = ?" for key in fields
        )

    query += " GROUP BY invoices.BillingCountry"

    params = [fields[key] for key in fields]

    record = execute_query(query, params)

    return jsonify({"sales": record})


if __name__ == "__main__":
    app.run(debug=True)
