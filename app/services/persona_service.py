from app.models.persona import Persona
from app.extensions import db


def get_personas():
    return Persona.query.all()


def get_persona_by_id(persona_id):
    return db.session.get(Persona, persona_id)


def create_persona(data):
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    email = data.get('email')
    if not nombre or not apellido or not email:
        return {'error': 'nombre, apellido y email son requeridos'}
    new_persona = Persona(nombre=nombre, apellido=apellido, email=email)
    db.session.add(new_persona)
    db.session.commit()
    return {'message': 'Persona agregada exitosamente'}


def update_persona(persona_id, data):
    persona = db.session.get(Persona, persona_id)
    if not persona:
        return {'error': 'Persona no encontrada'}
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    email = data.get('email')
    if not nombre or not apellido or not email:
        return {'error': 'nombre, apellido y email son requeridos'}
    persona.nombre = nombre
    persona.apellido = apellido
    persona.email = email
    db.session.commit()
    return {'message': 'Persona actualizada exitosamente'}


def delete_persona(persona_id):
    persona = db.session.get(Persona, persona_id)
    if not persona:
        return {'error': 'Persona no encontrada'}
    db.session.delete(persona)
    db.session.commit()
    return {'message': 'Persona eliminada exitosamente'}
