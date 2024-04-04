# flask_proof_of_concept_sqlite

# Instructions
1. python virtualenv venv
2. source venv/bin/activate
3. pip install -r requirements.txt

# Create db
4. flask shell
 >>> db.create_all()

# if required (previously)
 >>> db.drop_all()

# if required
 python fake.py  -> populate db

# run application
5. python app.py

# get all
6. curl http://localhost:5555/personas

# get one
7. curl http://localhost:5555/personas/1
