from flask_restful import Api
from app.controllers.persona_controller import Personas


def init_routes(app):
    api = Api(app)
    api.add_resource(Personas, '/personas', '/personas/<int:persona_id>')
