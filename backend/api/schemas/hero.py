# backend/api/schemas/hero.py

from flask_restx import Namespace, fields

hero_ns = Namespace('heroes', description='Hero operations')

hero_model = hero_ns.model('Hero', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a hero'),
    'name': fields.String(required=True, description='Name of the hero'),
    #'heroNumber': fields.Integer(required=False, description='Unique number of the hero within the town'),
    'image': fields.String(description='Image URL of the hero'),
    #'spriteSheet': fields.String(description='Sprite sheet URL of the hero'),
    'heroClass': fields.String(description='Class of the hero'),
    'heroGroup': fields.Integer(required=True, description='Group number (1 or 2)', enum=[1, 2]),
    #'passive': fields.String(description='Passive ability of the hero'),
    'stats': fields.Raw(description='Statistics of the hero'),
    'level': fields.Integer(required=True, description='Level of the hero'),
    'experience': fields.Integer(required=True, description='Experience points of the hero'),
    'requiredExperience': fields.Integer(required=True, description='Experience required for next level'),
    'x': fields.Integer(description='X-coordinate position'),
    'y': fields.Integer(description='Y-coordinate position'),
    #'sprite': fields.String(required=False, description='Sprite information')
})
