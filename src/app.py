from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
from geopy.geocoders import Nominatim

app = Flask(__name__)
api = Api(app)


class Address(Resource):

    def 

    def get(self):
        geolocator = Nominatim(user_agent="my-app")
        add_to_search = request.args.get('add')
        if add_to_search is not None:
            print(request.args, request.args.add, add_to_search)
            location = geolocator.geocode(add_to_search)
            coordinates = {'lat': location.latitude, 'lng':location.longitude}
            return jsonify({'coordinates':coordinates, 'address':add_to_search})
        else:
            return jsonify({'error':'please enter proper address'})


api.add_resource(Address, '/loc')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)