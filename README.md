# flask_proof_of_concept_sqlite

# Instructions
1. python -m virtualenv venv | python -m venv venv
2. source venv/bin/activate | .\venv\Scripts\activate
3. pip install -r requirements.txt

# Create db
4. flask shell
   
 shell> db.create_all()

# if required (previously)
 shell> db.drop_all()

# if required
 python fake.py  -> populate db

# run application
5. python app.py

# get all
6. curl http://localhost:5555/personas

# get one
7. curl http://localhost:5555/personas/1
