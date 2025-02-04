from flask_restx import Namespace, Resource, fields

initial_hero_ns = Namespace('initial_hero', description='Initial hero stats')


passive_model = initial_hero_ns.model('Passive', {
    'name': fields.String(description='Name of the passive'),
    'description': fields.String(description='Passive description'),
})

hero_model = initial_hero_ns.model('Hero', {
    'name': fields.String(description='Name of the hero'),
    'image': fields.String(description='Animated image URL'),
    'spriteSheet': fields.String(description='Sprite sheet URL'),
    'passive': fields.Nested(passive_model),
    'stats': fields.Raw(description='Hero statistics'),
})
