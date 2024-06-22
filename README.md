# flask_proof_of_concept_sqlite

## Instructions to start
~~~bash
python -m virtualenv venv | python -m venv venv
source venv/bin/activate | .\venv\Scripts\activate
pip install -r requirements.txt
~~~

## Run application
~~~bash
python run.py
~~~

### Populate db
~~~bash
python -m scripts.fake
~~~

### Get all
~~~bash
curl --request GET --url http://localhost:5555/personas
~~~

### Get one
~~~bash
curl --request GET --url http://localhost:5555/personas/1
~~~

### Create
~~~bash
curl --request POST --url http://localhost:5555/personas --header 'Content-Type: application/json' --data '{"nombre": "Juan", "apellido": "Perez", "email": "juan@perez.com"}'
~~~

### Update
~~~bash
curl --request PUT --url http://localhost:5555/personas/1 --header 'Content-Type: application/json' --data '{"nombre": "Juan", "apellido": "Perez", "email": "juancito@perez.com"}'
~~~

### Delete
~~~bash
curl --request DELETE --url http://localhost:5555/personas/11
~~~

### Test
~~~bash
python -m unittest discover -s tests
~~~
