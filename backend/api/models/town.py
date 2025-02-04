from uuid import uuid4
from datetime import datetime
from sqlalchemy import CheckConstraint
from backend.api.models.db import db
from backend.api.models.user import User

class Town(db.Model):
    __tablename__ = 'towns'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), default=lambda: str(uuid4()), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationship to User
    user = db.relationship('User', backref=db.backref('towns', lazy='dynamic'))

    # Relationship to Heroes
    heroes = db.relationship('Hero', backref='town', cascade='all, delete-orphan', lazy='dynamic')

    def __repr__(self):
        return f"<Town {self.name} owned by User ID {self.user_id}>"

    def to_dict(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'heroes': [hero.to_dict() for hero in self.heroes.all()]
        }
