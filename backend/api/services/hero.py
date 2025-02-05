from backend.api.models.hero import Hero
from backend.api.models.town import Town
from backend.api.models.db import db
from backend.api.game.data.heroes import NewHeroStats

class HeroService:
    MAX_HEROES_PER_TOWN = 10
    MAX_HEROES_PER_GROUP = 5

    @staticmethod
    def get_hero_stats():
        return NewHeroStats

    @staticmethod
    def add_hero(town: Town, hero_data: dict):
        current_hero_count = town.heroes.count()
        if current_hero_count >= HeroService.MAX_HEROES_PER_TOWN:
            return {'message': f'Town cannot have more than {HeroService.MAX_HEROES_PER_TOWN} heroes.'}, 400
        hero_group = hero_data.get('heroGroup')
        if hero_group not in [1, 2]:
            return {'message': 'Invalid hero group. Must be 1 or 2.'}, 400
        group_count = town.heroes.filter_by(hero_group=hero_group).count()
        if group_count >= HeroService.MAX_HEROES_PER_GROUP:
            return {'message': f'Group {hero_group} cannot have more than {HeroService.MAX_HEROES_PER_GROUP} heroes.'}, 400
        stats = hero_data.get('stats', {})
        hero = Hero(
            name=hero_data.get('name'),
            image=hero_data.get('image'),
            hero_class=hero_data.get('heroClass'),
            hero_group=hero_group,
            passive=hero_data.get('passive.description'),
            health=stats.get('Health', 100),
            fire_attack=stats.get('Fire Attack', 10),
            water_attack=stats.get('Water Attack', 10),
            light_attack=stats.get('Light Attack', 10),
            dark_attack=stats.get('Dark Attack', 10),
            fire_defense=stats.get('Fire Defense', 10),
            water_defense=stats.get('Water Defense', 10),
            light_defense=stats.get('Light Defense', 10),
            dark_defense=stats.get('Dark Defense', 10),
            attack_speed=stats.get('Attack Speed', 1.0),
            level=hero_data.get('level', 1),
            experience=hero_data.get('experience', 0),
            required_experience=hero_data.get('requiredExperience', 100),
            x=hero_data.get('x', 0),
            y=hero_data.get('y', 0),
            sprite=hero_data.get('sprite'),
            town=town
        )
        db.session.add(hero)
        db.session.commit()
        return hero.to_dict(), 201

    @staticmethod
    def get_heroes(town: Town):
        heroes = town.heroes.all()
        return [hero.to_dict() for hero in heroes], 200

    @staticmethod
    def update_hero(town: Town, hero_id: int, hero_data: dict):
        hero = town.heroes.filter_by(id=hero_id).first()
        if not hero:
            return {'message': 'Hero not found.'}, 404
        allowed_fields = {'name', 'image', 'heroClass', 'heroGroup', 'level', 'experience', 'requiredExperience', 'x', 'y', 'sprite'}
        allowed_stats = {'health', 'fire_attack', 'water_attack', 'light_attack', 'dark_attack', 'fire_defense', 'water_defense', 'light_defense', 'dark_defense', 'attack_speed'}
        for key, value in hero_data.items():
            if key == 'stats' and isinstance(value, dict):
                for stat_key, stat_value in value.items():
                    key_normalized = stat_key.lower().replace(' ', '_')
                    if key_normalized in allowed_stats:
                        setattr(hero, key_normalized, stat_value)
            elif key in allowed_fields:
                setattr(hero, key.lower(), value)
        db.session.commit()
        return hero.to_dict(), 200

    @staticmethod
    def delete_hero(town: Town, hero_id: int):
        hero = town.heroes.filter_by(id=hero_id).first()
        if not hero:
            return {'message': 'Hero not found.'}, 404
        db.session.delete(hero)
        db.session.commit()
        return {'message': 'Hero deleted successfully.'}, 200
