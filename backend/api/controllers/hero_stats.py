
from flask_restx import Namespace, Resource, fields
from backend.api.game.data.heroes import NewHeroStats
from backend.api.services.hero import HeroService
from backend.api.schemas.hero_stats import initial_hero_ns, passive_model, hero_model
from flask_security import login_required

hero_stats_ns = initial_hero_ns

def serialize_hero(hero):
    serialized = hero.copy()
    passive = serialized.get("passive", {})
    serialized["passive"] = {
        "name": passive.get("name", ""),
        "description": passive.get("description", "")
    }
    return serialized

@hero_stats_ns.route('/hero_stats')
class InitialHeroStatsController(Resource):
    @initial_hero_ns.doc("list_initial_hero_stats")
    @login_required
    @initial_hero_ns.marshal_list_with(hero_model)
    def get(self):
        """List all initial hero data"""
        hero_data = HeroService.get_hero_stats()
        serialized_data = [serialize_hero(hero) for hero in hero_data]
        return serialized_data, 200