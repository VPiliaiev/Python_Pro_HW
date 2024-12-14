from flask import Flask, jsonify
from webargs import fields as webargs_fields
from webargs.flaskparser import use_kwargs
from database_handler import execute_query

app = Flask(__name__)


@app.route("/get-all-info-about-track")
@use_kwargs(
    {
        "id": webargs_fields.Int(missing=None),
    },
    location="query")
def get_all_info_about_track(id):
    query = """
    SELECT 
        tracks.TrackId, 
        tracks.Name AS TrackName, 
        tracks.Composer, 
        tracks.Milliseconds, 
        tracks.Bytes, 
        tracks.UnitPrice,
        albums.AlbumId, 
        albums.Title AS AlbumTitle,
        artists.ArtistId, 
        artists.Name AS ArtistName,
        genres.GenreId, 
        genres.Name AS GenreName,
        media_types.MediaTypeId, 
        media_types.Name AS MediaTypeName,
        GROUP_CONCAT(DISTINCT playlists.Name) AS PlaylistNames,
        SUM(invoice_items.UnitPrice * invoice_items.Quantity) AS Sales
    FROM tracks
    INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
    INNER JOIN artists ON albums.ArtistId = artists.ArtistId
    INNER JOIN genres ON tracks.GenreId = genres.GenreId
    INNER JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
    LEFT JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
    LEFT JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
    LEFT JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
    LEFT JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
    """

    fields = {}
    if id:
        fields['tracks.TrackId'] = id

    if fields:
        query += " WHERE " + " AND ".join(
            f"{key} = ?" for key in fields
        )

    query += " GROUP BY tracks.TrackId;"

    data = execute_query(query, tuple(fields.values()))

    return jsonify({"track_info": data})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
