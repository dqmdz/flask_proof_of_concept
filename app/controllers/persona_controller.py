from flask_restful import Resource
from flask import request
from app.services.persona_service import get_personas, get_persona_by_id, create_persona, update_persona, delete_persona


class Personas(Resource):

    def get(self, persona_id=None):
        if persona_id:
            persona = get_persona_by_id(persona_id)
            if not persona:
                return {'error': 'Persona not found'}, 404
            return {'persona': persona.to_dict()}, 200
        else:
            personas = get_personas()
            return {'personas': [persona.to_dict() for persona in personas]}, 200

    def post(self):
        data = request.get_json()
        result = create_persona(data)
        if result.get('error'):
            return result, 400
        return result, 201

    def put(self, persona_id):
        data = request.get_json()
        result = update_persona(persona_id, data)
        if result.get('error'):
            return result, 400
        return result, 200

    def delete(self, persona_id):
        result = delete_persona(persona_id)
        if result.get('error'):
            return result, 404
        return result, 200
