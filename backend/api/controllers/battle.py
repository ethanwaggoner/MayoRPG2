from flask import request
from flask_restx import Resource
from flask_security import current_user, login_required
from backend.api.schemas.battle import (
    battle_ns,
    battle_model,
    battle_create_model,
    battle_validation_model,
    battle_completion_model
)
from backend.api.services.battle import BattleService
from backend.api.limiter import limiter

@battle_ns.route('/')
class BattleListController(Resource):
    @battle_ns.doc('create_battle')
    @battle_ns.expect(battle_create_model, validate=True)
    @battle_ns.marshal_with(battle_model, code=201)
    @battle_ns.response(400, 'Validation Error')
    @battle_ns.response(404, 'Town not found')
    @login_required
    @limiter.limit("30/minute")
    def post(self):
        """Create a new battle"""
        data = request.get_json()
        response, status = BattleService.create_battle(current_user, data)
        return response, status

@battle_ns.route('/<string:battle_uuid>/')
@battle_ns.param('battle_uuid', 'The UUID of the battle')
class BattleController(Resource):
    @battle_ns.doc('get_battle')
    @battle_ns.marshal_with(battle_model)
    @battle_ns.response(404, 'Battle not found')
    @login_required
    def get(self, battle_uuid):
        """Get a battle by UUID"""
        response, status = BattleService.get_battle(current_user, battle_uuid)
        return response, status

@battle_ns.route('/<string:battle_uuid>/validate/')
@battle_ns.param('battle_uuid', 'The UUID of the battle')
class BattleValidationController(Resource):
    @battle_ns.doc('validate_turn')
    @battle_ns.expect(battle_validation_model, validate=True)
    @battle_ns.response(200, 'Turn validated')
    @battle_ns.response(400, 'Validation Error')
    @battle_ns.response(404, 'Battle not found')
    @login_required
    @limiter.limit("60/minute")
    def post(self, battle_uuid):
        """Validate a battle turn"""
        data = request.get_json()
        response, status = BattleService.validate_turn(current_user, battle_uuid, data)
        return response, status

@battle_ns.route('/<string:battle_uuid>/complete/')
@battle_ns.param('battle_uuid', 'The UUID of the battle')
class BattleCompletionController(Resource):
    @battle_ns.doc('complete_battle')
    @battle_ns.expect(battle_completion_model, validate=True)
    @battle_ns.response(200, 'Battle completed')
    @battle_ns.response(400, 'Validation Error')
    @battle_ns.response(404, 'Battle not found')
    @login_required
    def post(self, battle_uuid):
        """Complete a battle and calculate rewards"""
        data = request.get_json()
        response, status = BattleService.complete_battle(current_user, battle_uuid, data)
        return response, status

@battle_ns.route('/town/<string:town_uuid>/')
@battle_ns.param('town_uuid', 'The UUID of the town')
class TownBattlesController(Resource):
    @battle_ns.doc('get_town_battles')
    @battle_ns.marshal_list_with(battle_model)
    @battle_ns.response(404, 'Town not found')
    @login_required
    def get(self, town_uuid):
        """Get all battles for a town"""
        response, status = BattleService.get_town_battles(current_user, town_uuid)
        return response, status