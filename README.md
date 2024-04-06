# flask_proof_of_concept_sqlite

# MySQL
```
docker compose up -d
```

# Instructions
1. python virtualenv venv
2. source venv/bin/activate
3. pip install -r requirements.txt (**include mysql-connector-python**)

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