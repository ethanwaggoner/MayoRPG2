from sqlalchemy import UniqueConstraint, CheckConstraint
from backend.api.models.db import db
from backend.api.models.town import Town

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    hero_number = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String(255))
    sprite_sheet = db.Column(db.String(255), nullable=True)
    hero_class = db.Column(db.String(100))
    hero_group = db.Column(db.Integer, nullable=False)  # 1 or 2
    passive = db.Column(db.String(255), nullable=True)

    # Stats
    health = db.Column(db.Integer, nullable=False, default=100)
    fire_attack = db.Column(db.Integer, nullable=False, default=10)
    water_attack = db.Column(db.Integer, nullable=False, default=10)
    light_attack = db.Column(db.Integer, nullable=False, default=10)
    dark_attack = db.Column(db.Integer, nullable=False, default=10)
    fire_defense = db.Column(db.Integer, nullable=False, default=10)
    water_defense = db.Column(db.Integer, nullable=False, default=10)
    light_defense = db.Column(db.Integer, nullable=False, default=10)
    dark_defense = db.Column(db.Integer, nullable=False, default=10)
    attack_speed = db.Column(db.Float, nullable=False, default=1.0)

    # Position and Level
    x = db.Column(db.Integer, default=0)
    y = db.Column(db.Integer, default=0)
    sprite = db.Column(db.String(255))

    # Progress
    level = db.Column(db.Integer, nullable=False, default=1)
    experience = db.Column(db.Integer, nullable=False, default=0)
    required_experience = db.Column(db.Integer, nullable=False, default=100)

    # Foreign Key to Town
    town_id = db.Column(db.Integer, db.ForeignKey('towns.id'), nullable=False)

    __table_args__ = (
        CheckConstraint('hero_group IN (1, 2)', name='check_hero_group'),
        UniqueConstraint('town_id', 'hero_number', name='unique_hero_number_per_town')
    )

    def __repr__(self):
        return f"<Hero {self.name} (Group {self.hero_group}) in Town ID {self.town_id}>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'heroNumber': self.hero_number,
            'image': self.image,
            'spriteSheet': self.sprite_sheet,
            'heroClass': self.hero_class,
            'heroGroup': self.hero_group,
            'passive': self.passive,
            'stats': {
                "Health": self.health,
                "Fire Attack": self.fire_attack,
                "Water Attack": self.water_attack,
                "Light Attack": self.light_attack,
                "Dark Attack": self.dark_attack,
                "Fire Defense": self.fire_defense,
                "Water Defense": self.water_defense,
                "Light Defense": self.light_defense,
                "Dark Defense": self.dark_defense,
                "Attack Speed": self.attack_speed
            },
            'level': self.level,
            'experience': self.experience,
            'requiredExperience': self.required_experience,
            'x': self.x,
            'y': self.y,
            'sprite': self.sprite
        }
