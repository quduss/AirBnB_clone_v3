#!/usr/bin/python3
"""define a route /status on the app_views blueprint"""
from flask import jsonify
from . import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def status():
    """returns json format of {"status": 'OK'}"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stat():
    """returns the number of each objects in storage by type"""
    dict_ = {
                "amenities": storage.count(Amenity),
                "cities": storage.count(City),
                "places": storage.count(Place),
                "reviews": storage.count(Review),
                "states": storage.count(State),
                "users": storage.count(User)
            }
    return jsonify(dict_)
