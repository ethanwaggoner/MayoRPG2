# backend/api/services/town.py

from backend.api.models.town import Town
from backend.api.models.user import User
from backend.api.models.db import db
from sqlalchemy.exc import IntegrityError

class TownService:
    MAX_TOWNS_PER_USER = 5

    @staticmethod
    def create_town(user: User, town_data: dict):
        if user.towns.count() >= TownService.MAX_TOWNS_PER_USER:
            return {'message': f'User cannot have more than {TownService.MAX_TOWNS_PER_USER} towns.'}, 400

        town = Town(
            name=town_data.get('name'),
            user=user
        )
        db.session.add(town)
        try:
            db.session.commit()
            return town.to_dict(), 201
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Error creating town. Possibly duplicate name.'}, 400

    @staticmethod
    def get_towns(user: User):
        towns = user.towns.all()
        return [town.to_dict() for town in towns], 200

    @staticmethod
    def get_town_by_uuid(user: User, town_uuid: str):
        town = user.towns.filter_by(uuid=town_uuid).first()
        if not town:
            return {'message': 'Town not found.'}, 404
        return town.to_dict(), 200

    @staticmethod
    def delete_town(user: User, town_uuid: str):
        town = user.towns.filter_by(uuid=town_uuid).first()
        if not town:
            return {'message': 'Town not found.'}, 404
        db.session.delete(town)
        db.session.commit()
        return {'message': 'Town deleted successfully.'}, 200
