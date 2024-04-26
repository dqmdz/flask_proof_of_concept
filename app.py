from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Persona

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)


class Personas(Resource):

    # read
    def get(self, persona_id=None):
        if persona_id:
            persona = db.session.get(Persona, persona_id)
            if not persona:
                return {'error': 'Persona not found'}, 404
            return {'persona': persona.to_dict()}, 200
        else:
            personas = Persona.query.all()
            return {'personas': [persona.to_dict() for persona in personas]}, 200

    # create
    def post(self):
        data = request.get_json()
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        email = data.get('email')
        if not nombre or not apellido or not email:
            return {'error': 'nombre and apellido and email are required'}, 400
        new_persona = Persona(nombre=nombre, apellido=apellido, email=email)
        db.session.add(new_persona)
        db.session.commit()
        return {'message': 'Persona added successfully'}, 201

    # update
    def put(self, persona_id):
        persona = db.session.get(Persona, persona_id)
        if not persona:
            return {'error': 'Persona not found'}, 404
        data = request.get_json()
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        email = data.get('email')
        if not nombre or not apellido or not email:
            return {'error': 'nombre and apellido and email are required'}, 400
        persona.nombre = nombre
        persona.apellido = apellido
        persona.email = email
        db.session.commit()
        return {'message': 'Persona updated successfully'}, 200

    # delete
    def delete(self, persona_id):
        persona = db.session.get(Persona, persona_id)
        if not persona:
            return {'error': 'Persona not found'}, 404
        db.session.delete(persona)
        db.session.commit()
        return {'message': 'Persona deleted successfully'}, 200


# use api.add_resource to add the paths
api.add_resource(Personas, '/personas', '/personas/<int:persona_id>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)
