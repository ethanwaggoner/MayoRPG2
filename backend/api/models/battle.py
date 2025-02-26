from uuid import uuid4
from datetime import datetime
from backend.api.models.db import db
from backend.api.models.town import Town


class Battle(db.Model):
    __tablename__ = 'battles'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), default=lambda: str(uuid4()), unique=True, nullable=False)
    town_id = db.Column(db.Integer, db.ForeignKey('towns.id'), nullable=False)
    status = db.Column(db.String(20), default='in_progress')
    battle_seed = db.Column(db.Integer, nullable=False)
    enemy_composition = db.Column(db.Text, nullable=False)
    difficulty_level = db.Column(db.Integer, default=1)


    enemy_scaling = db.Column(db.Float, default=1.0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)

    results = db.Column(db.Text, nullable=True)  # JSON string of battle results

    town = db.relationship('Town', backref=db.backref('battles', lazy='dynamic'))

    events = db.relationship('BattleEvent', backref='battle', cascade='all, delete-orphan', lazy='dynamic')

    def __repr__(self):
        return f"<Battle {self.uuid} for Town {self.town_id}>"

    def to_dict(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'town_id': self.town_id,
            'status': self.status,
            'battle_seed': self.battle_seed,
            'enemy_composition': self.enemy_composition,
            'difficulty_level': self.difficulty_level,
            'enemy_scaling': self.enemy_scaling,
            'created_at': self.created_at.isoformat(),
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'results': self.results
        }


class BattleEvent(db.Model):
    __tablename__ = 'battle_events'

    id = db.Column(db.Integer, primary_key=True)
    battle_id = db.Column(db.Integer, db.ForeignKey('battles.id'), nullable=False)
    turn = db.Column(db.Integer, nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    actor_id = db.Column(db.String(50), nullable=False)
    target_id = db.Column(db.String(50), nullable=True)
    data = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<BattleEvent {self.id} - {self.event_type} by {self.actor_id}>"

    def to_dict(self):
        return {
            'id': self.id,
            'battle_id': self.battle_id,
            'turn': self.turn,
            'event_type': self.event_type,
            'actor_id': self.actor_id,
            'target_id': self.target_id,
            'data': self.data,
            'timestamp': self.timestamp.isoformat()
        }