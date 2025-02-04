from flask_restx import Api

from backend.api.controllers import auth, hero, town, hero_stats

api = Api(version='Alpha 0.1', prefix='/api', title='MayoRPG2API', description='pewpew')

api.add_namespace(auth.auth)
api.add_namespace(hero.hero_ns)
api.add_namespace(hero_stats.hero_stats_ns)
api.add_namespace(town.town_ns)


