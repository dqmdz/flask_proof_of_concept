from faker import Faker
from run import create_app
from app.extensions import db
from app.models.persona import Persona

fake = Faker()
app = create_app()

with app.app_context():
    print("Starting seed...")
    Persona.query.delete()
    new_personas = []
    for _ in range(10):
        nombre = fake.first_name()
        apellido = fake.last_name()
        email = fake.email()
        new_persona = Persona(nombre=nombre, apellido=apellido, email=email)
        new_personas.append(new_persona)
    db.session.add_all(new_personas)
    db.session.commit()
    print("Successfully seeded")
