from faker import Faker
from app import app
from models import db, Persona

fake = Faker()
with app.app_context():
    print("Starting seed...")
    Persona.query.delete()
    new_personas = []
    for _ in range(10):
        nombre = fake.user_name()
        apellido = fake.name()
        email = fake.email()
        new_persona = Persona(nombre=nombre, apellido=apellido, email=email)
        new_personas.append(new_persona)
    db.session.add_all(new_personas)
    db.session.commit()
    print("Successfully seeded")
