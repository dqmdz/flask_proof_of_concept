import unittest
import json
from run import create_app
from app.extensions import db
from app.models.persona import Persona
from app.config import TestConfig


class TestPersona(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app(TestConfig)
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()

    def setUp(self):
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_all_personas(self):
        response = self.client.get('/personas')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['personas']), 0)

    def test_create_persona(self):
        data = {
            'nombre': 'John',
            'apellido': 'Doe',
            'email': 'john.doe@example.com'
        }
        response = self.client.post(
            '/personas', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'],
                         'Persona agregada exitosamente')

        personas = Persona.query.all()
        self.assertEqual(len(personas), 1)

    def test_get_persona(self):
        persona = Persona(nombre='John', apellido='Doe',
                          email='john.doe@example.com')
        db.session.add(persona)
        db.session.commit()
        response = self.client.get(f'/personas/{persona.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['persona']['nombre'], 'John')

    def test_update_persona(self):
        persona = Persona(nombre='John', apellido='Doe',
                          email='john.doe@example.com')
        db.session.add(persona)
        db.session.commit()
        data = {
            'nombre': 'Jane',
            'apellido': 'Doe',
            'email': 'jane.doe@example.com'
        }
        response = self.client.put(
            f'/personas/{persona.id}', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'],
                         'Persona actualizada exitosamente')

        updated_persona = Persona.query.first()
        self.assertEqual(updated_persona.nombre, 'Jane')

    def test_delete_persona(self):
        persona = Persona(nombre='John', apellido='Doe',
                          email='john.doe@example.com')
        db.session.add(persona)
        db.session.commit()
        response = self.client.delete(f'/personas/{persona.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'],
                         'Persona eliminada exitosamente')

        personas = Persona.query.all()
        self.assertEqual(len(personas), 0)


if __name__ == '__main__':
    unittest.main()
