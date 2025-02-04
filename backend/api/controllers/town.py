from flask import request, session
from flask_restx import Resource
from flask_security import current_user, login_required
from backend.api.schemas.town import town_ns, town_model
from backend.api.services.town import TownService


@town_ns.route('/')
class TownListController(Resource):
    @town_ns.doc('list_towns')
    @town_ns.marshal_list_with(town_model)
    @login_required
    def get(self):
        """List all towns for the current user"""
        towns, status = TownService.get_towns(current_user)
        return towns, status

    @town_ns.expect(town_model, validate=True)
    @town_ns.marshal_with(town_model, code=201)
    @town_ns.response(400, 'Validation Error')
    @login_required
    def post(self):
        """Create a new town"""
        data = request.get_json()
        response, status = TownService.create_town(current_user, data)
        return response, status

@town_ns.route('/<string:town_uuid>/')
@town_ns.param('town_uuid', 'The UUID of the town')
class TownController(Resource):
    @town_ns.doc('get_town')
    @town_ns.marshal_with(town_model)
    @town_ns.response(404, 'Town not found')
    @login_required
    def get(self, town_uuid):
        """Get a town by UUID"""

        if not town_uuid:
            town_uuid = session["town_uuid"]

        response, status = TownService.get_town_by_uuid(current_user, town_uuid)
        session["town_uuid"] = town_uuid
        return response, status

    @town_ns.doc('delete_town')
    @town_ns.response(200, 'Town deleted successfully')
    @town_ns.response(404, 'Town not found')
    @login_required
    def delete(self, town_uuid):
        response, status = TownService.delete_town(current_user, town_uuid)
        return response, status
