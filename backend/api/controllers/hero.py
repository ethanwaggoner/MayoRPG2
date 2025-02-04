from flask import request, session
from flask_restx import Resource
from flask_security import current_user, login_required
from backend.api.schemas.hero import hero_ns, hero_model
from backend.api.services.town import TownService
from backend.api.services.hero import HeroService
from backend.api.models.town import Town

@hero_ns.route('/<string:town_uuid>/')
@hero_ns.param('town_uuid', 'The UUID of the town')
class HeroListController(Resource):
    @hero_ns.doc("list_initial_hero_stats")
    @login_required
    def get(self):
        """List all initial hero data"""
        hero_data = HeroService.get_hero_stats()
        return hero_data, 200


    @hero_ns.doc('list_heroes')
    @hero_ns.marshal_list_with(hero_model)
    @hero_ns.response(404, 'Town not found')
    @login_required
    def get(self, town_uuid):
        if town_uuid == "null":
            town_uuid = session.get("town_uuid")

        town_response, status = TownService.get_town_by_uuid(current_user, town_uuid)
        session["town_uuid"] = town_uuid
        if status != 200:
            return town_response, status

        town_instance = Town.query.filter_by(uuid=town_uuid, user_id=current_user.id).first()
        if not town_instance:
            return {'message': 'Town not found.'}, 404

        heroes, status = HeroService.get_heroes(town_instance)
        return heroes, status

    @hero_ns.expect(hero_model, validate=True)
    @hero_ns.marshal_with(hero_model, code=201)
    @hero_ns.response(400, 'Validation Error')
    @hero_ns.response(404, 'Town not found')
    @login_required
    def post(self, town_uuid):
        """Add a new hero to a town"""
        data = request.get_json()

        # Fetch the Town model instance
        town_instance = Town.query.filter_by(uuid=town_uuid, user_id=current_user.id).first()
        if not town_instance:
            return {'message': 'Town not found.'}, 404

        response, status = HeroService.add_hero(town_instance, data)
        return response, status

@hero_ns.route('/<string:town_uuid>/<int:hero_id>/')
@hero_ns.param('town_uuid', 'The UUID of the town')
@hero_ns.param('hero_id', 'The ID of the hero')
class HeroController(Resource):
    @hero_ns.doc('update_hero')
    @hero_ns.expect(hero_model, validate=True)
    @hero_ns.marshal_with(hero_model)
    @hero_ns.response(400, 'Validation Error')
    @hero_ns.response(404, 'Hero not found')
    @login_required
    def put(self, town_uuid, hero_id):
        data = request.get_json()

        town_instance = Town.query.filter_by(uuid=town_uuid, user_id=current_user.id).first()
        if not town_instance:
            return {'message': 'Town not found.'}, 404

        response, status = HeroService.update_hero(town_instance, hero_id, data)
        return response, status

    @hero_ns.doc('delete_hero')
    @hero_ns.response(200, 'Hero deleted successfully')
    @hero_ns.response(404, 'Hero not found')
    @login_required
    def delete(self, town_uuid, hero_id):
        town_instance = Town.query.filter_by(uuid=town_uuid, user_id=current_user.id).first()
        if not town_instance:
            return {'message': 'Town not found.'}, 404

        response, status = HeroService.delete_hero(town_instance, hero_id)
        return response, status
