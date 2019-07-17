from flask import jsonify, abort
from flask_restful import Resource, reqparse, fields, marshal
from .models import Places, db, IntegrityError
import json

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
        
        try:
            db.session.add(create_place)
            db.session.commit()
        except IntegrityError:
                abort(409, 'Conflict')
               
        if create_place:
            return json.dumps({'success':True}), 201, {'ContentType':'application/json'} 
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
            abort(404, 'Not Found')

    def put(self, id):
        id_parser = reqparse.RequestParser()
        id_parser.add_argument('id', location='view_args', required = True)
        id_args = id_parser.parse_args()
        
        get_place_id = db.session.query(Places.id).filter(Places.id == id_args['id'])
        place_id = get_place_id.first()
        
        if place_id:
            name_parser = reqparse.RequestParser()
            name_parser.add_argument('name', location='json', required = True)
            name_args = name_parser.parse_args()
            
            update_place = Places.query.get(id_args['id'])
            update_place.name = name_args['name']
            
            try:
                db.session.commit()
            except IntegrityError:
                abort(409, 'Conflict')
            
            if update_place:
                return json.dumps({'success':True}), 201, {'ContentType':'application/json'} 
            else:
                abort(400, 'Bad Request')
        else:
            abort(404, 'Not Found')
            
    def delete(self, id):
        id_parser = reqparse.RequestParser()
        id_parser.add_argument('id', location='view_args', required = True)
        id_args = id_parser.parse_args()

        delete_place = Places.query.filter_by(id = id_args['id']).delete()
        db.session.commit()
       
        if delete_place:
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        else:
            abort(404, 'Not Found')