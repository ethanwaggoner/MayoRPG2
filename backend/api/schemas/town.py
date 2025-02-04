from flask_restx import Namespace, fields

from backend.api.schemas.hero import hero_model

town_ns = Namespace('towns', description='Town operations')

town_model = town_ns.model('Town', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a town'),
    'uuid': fields.String(readOnly=True, description='Unique UUID of the town'),
    'name': fields.String(required=True, description='Name of the town'),
    'created_at': fields.DateTime(readOnly=True, description='Time when the town was created'),
    'heroes': fields.List(fields.Nested(hero_model), description='List of heroes in the town')
})
