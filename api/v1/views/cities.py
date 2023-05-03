#!/usr/bin/python3
""" view for City objects"""
from api.v1.views import app_views
from flask import request, jsonify, abort
from models.city import City
from models import storage


@app_views.route('/cities',
                 methods=['GET', 'POST'], strict_slashes=False)
@app_views.route('/cities/<state_id>',
                 methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def cities(state_id=None):
    """Retrieves a list of city objects"""

    city_objs = storage.all(City)

    cities = [obj.to_dict() for obj in city_objs.values()]
    if not state_id:
        if request.method == 'GET':
            return jsonify(cities)
        elif request.method == 'POST':
            data = request.get_json()

            if data is None:
                abort(400, 'Not a JSON')
            if data.get("name") is None:
                abort(400, 'Missing name')
            new = City(**data)
            new.save()
            return jsonify(new.to_dict()), 201
    else:
        if request.method == 'GET':
            for city in cities:
                if city.get('id') == state_id:
                    return jsonify(city)
            abort(404)
        elif request.method == 'PUT':
            data = request.get_json()

            if data is None:
                abort(400, 'Not a JSON')

            for city in city_objs.values():
                if state.id == state_id:
                    city.name = data.get("name")
                    city.save()
                    return jsonify(city.to_dict()), 200
            abort(404)

        elif request.method == 'DELETE':
            for obj in city_objs.values():
                if obj.id == city_id:
                    storage.delete(obj)
                    storage.save()
                    return jsonify({}), 200
            abort(404)
