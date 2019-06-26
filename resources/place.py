from flask import jsonify, abort
from flask_restful import Resource, reqparse, fields, marshal
from .models import Places, db

place_fields = {
    'id':   fields.Integer,
    'name': fields.String,
}

class Place(Resource):
    def get(self):
        json = [marshal(place, place_fields) for place in Places.query.order_by(Places.id).all()]
        return jsonify(json)
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required = True)
        args = parser.parse_args()
        
        create_place = Places(name = args['name'])
        db.session.add(create_place)
        db.session.commit()
               
        if create_place:
            return 'Successful'
        else:
            abort(400, 'Bad Request')
    
class PlaceById(Resource):
    def get(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('id', location='view_args', required = True)
        args = parser.parse_args()
        json = [marshal(place, place_fields) for place in Places.query.filter(Places.id == args['id'])]
       
        if json:
            return jsonify(json)
        else:
            abort(404, 'Place not found')

    def put(self, id):
        id_parser = reqparse.RequestParser()
        id_parser.add_argument('id', location='view_args', required = True)
        id_args = id_parser.parse_args()
        
        name_parser = reqparse.RequestParser()
        name_parser.add_argument('name', location='json', required = True)
        name_args = name_parser.parse_args()
        
        update_place = Places.query.get(id_args['id'])
        update_place.name = name_args['name']
        db.session.commit()
       
        if update_place:
            return 'Successful'
        else:
            abort(400, 'Bad Request')
            
    def delete(self, id):
        id_parser = reqparse.RequestParser()
        id_parser.add_argument('id', location='view_args', required = True)
        id_args = id_parser.parse_args()

        delete_place = Places.query.filter_by(id = id_args['id']).delete()
        db.session.commit()
       
        if delete_place:
            return 'Successful'
        else:
            abort(400, 'Bad Request')