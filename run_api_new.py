from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.serving import run_simple

from solr_connection import SolrConnection
from settings import APP_BIND_ADDRESS, APP_BIND_PORT, SOLR_COLLECTION_PATH



app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
connection = SolrConnection('http://localhost:8983/solr/mycol1')

@app.route("/api/search", methods=['GET'])
def search():
    query_text = request.args.get('q', default="", type=str)
    print(query_text    )
    results = connection.search(query_text, rows=50)
    print((results))
    return jsonify(list(results))



app.run(debug=True, host="0.0.0.0", port=1234)
