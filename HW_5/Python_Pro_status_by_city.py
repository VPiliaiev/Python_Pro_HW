from flask import Flask, jsonify
from webargs import fields as webargs_fields
from webargs.flaskparser import use_kwargs
from webargs import validate
from database_handler import execute_query

app = Flask(__name__)


@app.route("/stats-by-city")
@use_kwargs(
    {
        "genre": webargs_fields.Str(
            required=True,
            validate=[
                validate.Length(min=2, max=20, error="Genre must be between 2 and 20 characters"),
            ],
            error_messages={
                "required": "Genre is required",
                "length": "Genre must be between 2 and 20 characters",
            }
        ),
    },
    location="query")
def stats_by_city(genre):
    query = """
           SELECT City, COUNT(*) as listens
           FROM customers
           JOIN invoices ON customers.CustomerId = invoices.CustomerId
           JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
           JOIN tracks ON invoice_items.TrackId = tracks.TrackId
           JOIN genres ON tracks.GenreId = genres.GenreId
       """
    conditions = {}
    if genre:
        conditions['genres.Name'] = genre

    if conditions:
        query += " WHERE " + " AND ".join(
            f"{key} = ?" for key in conditions
        )

    query += " GROUP BY City ORDER BY listens DESC LIMIT 1;"

    data = execute_query(query, tuple(conditions.values()))

    city, listens = data[0]
    city_data = {
        "city": city,
        "listens": listens
    }

    return jsonify(city_data)


if __name__ == '__main__':
    app.run(debug=True, port=5001)


