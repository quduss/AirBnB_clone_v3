#!/usr/bin/python3
"""Start Flask app"""
from flask import Flask, jsonify, make_response
from api.v1.views import app_views
from models import storage
import os
from flask_cors import CORS
from flasgger import Swagger


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = int(os.getenv('HBNB_API_PORT', 5000))


@app.errorhandler(404)
def not_found_error(error):
    return make_response(jsonify({'error': "Not found"}), 404)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

Swagger(app)

# Run Flask application with specified host, port, and threaded=True
if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)
