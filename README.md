# flask_proof_of_concept_sqlite

# Instructions
1. python virtualenv venv
2. source venv/bin/activate
3. pip install -r requirements.txt

# Create db
4. flask shell
5. > > > db.create_all()

if required (previously)

4.1 > > > db.drop_all()

if required

6. python fake.py  -> populate db

# run application
7. python app.py

# get all
8. curl http://localhost:5555/personas

# get one
9. curl http://localhost:5555/personas/1
