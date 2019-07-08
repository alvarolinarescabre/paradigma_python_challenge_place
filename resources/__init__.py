from flask import Flask, redirect, url_for
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restful import Api
from resources.place import Place, PlaceById
from config import app_config
from .models import db
from . import place

def create_app(config_name):
   app = Flask(__name__, instance_relative_config = True)
   app.config.from_object(app_config[config_name])
   app.add_url_rule('/', endpoint='index')
   app.config['JSON_AS_ASCII'] = False
   app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

   # SQLAlchemy
   db.init_app(app)

   # Api Place
   api = Api(app)
   api.add_resource(Place, '/v1/places', methods=['GET','POST'])
   api.add_resource(PlaceById, '/v1/places/<id>', methods=['GET','PUT','DELETE'])

   # Swagger
   SWAGGER_URL = '/swagger'
   API_URL = '/static/swagger.json'
   SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
      SWAGGER_URL,
      API_URL,
   )

   app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

   @app.route('/')
   def index():
      return redirect(url_for('swagger_ui.show'))
   
   return app
