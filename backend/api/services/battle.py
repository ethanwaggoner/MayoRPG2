import json
import random
import math
from datetime import datetime
from backend.api.models.db import db
from backend.api.models.battle import Battle, BattleEvent
from backend.api.models.town import Town
from backend.api.models.hero import Hero


class BattleService:
    MAX_GRID_SIZE = 12  # Grid size (12x12)
    MAX_TURNS = 100  # Maximum turns before battle times out

    ENEMY_TEMPLATES = {
        'goblin': {
            'health': 50,
            'attack': 10,
            'defense': 5,
            'speed': 3
        },
        'orc': {
            'health': 100,
            'attack': 15,
            'defense': 10,
            'speed': 2
        },
        'troll': {
            'health': 200,
            'attack': 25,
            'defense': 15,
            'speed': 1
        }
    }

    @staticmethod
    def generate_battle_seed():
        return random.randint(100000, 999999)

    @staticmethod
    def generate_enemy_composition(difficulty_level, hero_count):
        enemy_count = min(30, math.ceil(difficulty_level * 1.5) + hero_count)

        enemies = []
        enemy_types = list(BattleService.ENEMY_TEMPLATES.keys())

        for i in range(enemy_count):
            # Higher difficulty means more challenging enemies
            weights = [
                max(0, 1.0 - (difficulty_level * 0.1)),  # Weaker enemies (goblin)
                min(0.8, 0.3 + (difficulty_level * 0.05)),  # Medium enemies (orc)
                min(0.5, 0.1 + (difficulty_level * 0.04))  # Strong enemies (troll)
            ]

            # Normalize weights
            total_weight = sum(weights)
            weights = [w / total_weight for w in weights]

            enemy_type = random.choices(enemy_types, weights=weights, k=1)[0]

            # Generate position
            position = {
                'x': random.randint(7, BattleService.MAX_GRID_SIZE - 1),
                'y': random.randint(0, BattleService.MAX_GRID_SIZE - 1)
            }

            # Create enemy with scaled stats based on difficulty
            enemy_base = BattleService.ENEMY_TEMPLATES[enemy_type].copy()
            scaling = 1.0 + (difficulty_level * 0.1)  # 10% increase per difficulty level

            enemies.append({
                'id': f"enemy_{i}",
                'type': enemy_type,
                'stats': {
                    'health': round(enemy_base['health'] * scaling),
                    'attack': round(enemy_base['attack'] * scaling),
                    'defense': round(enemy_base['defense'] * scaling),
                    'speed': enemy_base['speed']
                },
                'position': position
            })

        return enemies

    @staticmethod
    def create_battle(user, battle_data):
        """Create a new battle for a town"""
        town_uuid = battle_data.get('town_uuid')
        difficulty_level = battle_data.get('difficulty_level', 1)
        hero_ids = battle_data.get('hero_ids', [])

        # Get the town
        town = Town.query.filter_by(uuid=town_uuid, user_id=user.id).first()
        if not town:
            return {'message': 'Town not found.'}, 404

        # Validate heroes belong to this town
        heroes = []
        for hero_id in hero_ids:
            hero = Hero.query.filter_by(id=hero_id, town_id=town.id).first()
            if not hero:
                return {'message': f'Hero with ID {hero_id} not found or does not belong to this town.'}, 400
            heroes.append(hero)

        # Generate battle data
        battle_seed = BattleService.generate_battle_seed()
        enemy_composition = BattleService.generate_enemy_composition(difficulty_level, len(heroes))

        # Calculate enemy scaling based on hero levels and difficulty
        avg_hero_level = sum(hero.level for hero in heroes) / len(heroes) if heroes else 1
        enemy_scaling = 1.0 + ((avg_hero_level - 1) * 0.05) + ((difficulty_level - 1) * 0.1)

        # Create battle record
        battle = Battle(
            town_id=town.id,
            status='in_progress',
            battle_seed=battle_seed,
            enemy_composition=json.dumps(enemy_composition),
            difficulty_level=difficulty_level,
            enemy_scaling=enemy_scaling
        )

        db.session.add(battle)
        db.session.commit()

        # Format the response
        response_data = battle.to_dict()
        response_data['enemy_composition'] = enemy_composition

        # Generate initial hero positions (in the first few columns)
        hero_positions = []
        for i, hero in enumerate(heroes):
            position = {
                'x': random.randint(0, 2),
                'y': random.randint(0, BattleService.MAX_GRID_SIZE - 1)
            }
            hero_positions.append({
                'hero_id': hero.id,
                'position': position,
                'stats': hero.to_dict()['stats']
            })

        response_data['hero_positions'] = hero_positions

        return response_data, 201

    @staticmethod
    def validate_turn(user, battle_uuid, validation_data):
        """Validate a turn's actions for anti-cheat"""
        battle = Battle.query.join(Town).filter(
            Battle.uuid == battle_uuid,
            Town.user_id == user.id
        ).first()

        if not battle:
            return {'message': 'Battle not found.'}, 404

        if battle.status != 'in_progress':
            return {'message': 'Battle is not in progress.'}, 400

        # Get turn data
        turn = validation_data.get('turn')
        events = validation_data.get('events', [])
        game_state = validation_data.get('game_state', {})

        # Very simple validation for this example
        # In a real implementation, you would simulate the turn and compare results

        # Check if turn exceeds maximum
        if turn > BattleService.MAX_TURNS:
            battle.status = 'failed'
            battle.completed_at = datetime.utcnow()
            battle.results = json.dumps({
                'outcome': 'timeout',
                'turns_taken': turn,
                'message': 'Battle exceeded maximum turn limit.'
            })
            db.session.commit()
            return {'message': 'Battle failed due to timeout.'}, 400

        # Record battle events
        for event in events:
            battle_event = BattleEvent(
                battle_id=battle.id,
                turn=turn,
                event_type=event.get('event_type'),
                actor_id=event.get('actor_id'),
                target_id=event.get('target_id'),
                data=json.dumps(event.get('data', {}))
            )
            db.session.add(battle_event)

        db.session.commit()

        # Return validation result
        return {
            'turn': turn,
            'valid': True,
            'corrections': {}  # Any corrections to the client state would go here
        }, 200

    @staticmethod
    def complete_battle(user, battle_uuid, completion_data):
        """Complete a battle and calculate rewards"""
        battle = Battle.query.join(Town).filter(
            Battle.uuid == battle_uuid,
            Town.user_id == user.id
        ).first()

        if not battle:
            return {'message': 'Battle not found.'}, 404

        if battle.status != 'in_progress':
            return {'message': 'Battle is already completed.'}, 400

        # Extract completion data
        victory = completion_data.get('victory', False)
        turns_taken = completion_data.get('turns_taken', 0)
        surviving_heroes = completion_data.get('surviving_heroes', [])
        final_state = completion_data.get('final_state', {})

        # Update battle status
        battle.status = 'completed'
        battle.completed_at = datetime.utcnow()

        # Calculate rewards based on difficulty, victory, and turns taken
        base_xp = battle.difficulty_level * 50
        base_gold = battle.difficulty_level * 100

        # Apply modifiers
        if not victory:
            base_xp = max(10, base_xp // 4)  # 25% XP for defeat
            base_gold = max(5, base_gold // 10)  # 10% gold for defeat
        else:
            # Bonus for efficiency (completing in fewer turns)
            efficiency_bonus = max(0, 1 - (turns_taken / BattleService.MAX_TURNS))
            base_xp = int(base_xp * (1 + (efficiency_bonus * 0.5)))
            base_gold = int(base_gold * (1 + (efficiency_bonus * 0.3)))

        # Apply rewards to heroes
        heroes_updated = []
        for hero_id in surviving_heroes:
            hero = Hero.query.filter_by(id=hero_id, town_id=battle.town_id).first()
            if hero:
                # Add XP
                hero.experience += base_xp

                # Check for level up
                while hero.experience >= hero.required_experience:
                    hero.experience -= hero.required_experience
                    hero.level += 1
                    hero.required_experience = int(
                        hero.required_experience * 1.2)  # Increase XP required for next level

                    # Increase stats with level up
                    hero.health += int(hero.health * 0.1)  # 10% health increase
                    hero.fire_attack += int(hero.fire_attack * 0.08)  # 8% attack increase
                    hero.water_attack += int(hero.water_attack * 0.08)
                    hero.light_attack += int(hero.light_attack * 0.08)
                    hero.dark_attack += int(hero.dark_attack * 0.08)
                    hero.fire_defense += int(hero.fire_defense * 0.05)  # 5% defense increase
                    hero.water_defense += int(hero.water_defense * 0.05)
                    hero.light_defense += int(hero.light_defense * 0.05)
                    hero.dark_defense += int(hero.dark_defense * 0.05)

                heroes_updated.append({
                    'hero_id': hero.id,
                    'xp_gained': base_xp,
                    'new_level': hero.level,
                    'xp_progress': hero.experience,
                    'xp_required': hero.required_experience
                })

        # Store battle results
        battle.results = json.dumps({
            'victory': victory,
            'turns_taken': turns_taken,
            'xp_rewarded': base_xp,
            'gold_rewarded': base_gold,
            'heroes_updated': heroes_updated,
            'final_state': final_state
        })

        db.session.commit()

        # Return battle results
        return {
            'battle_uuid': battle.uuid,
            'victory': victory,
            'xp_rewarded': base_xp,
            'gold_rewarded': base_gold,
            'heroes_updated': heroes_updated
        }, 200

    @staticmethod
    def get_battle(user, battle_uuid):
        """Get a battle by UUID"""
        battle = Battle.query.join(Town).filter(
            Battle.uuid == battle_uuid,
            Town.user_id == user.id
        ).first()

        if not battle:
            return {'message': 'Battle not found.'}, 404

        # Format the response
        response_data = battle.to_dict()

        # Parse JSON strings to objects
        if response_data['enemy_composition']:
            response_data['enemy_composition'] = json.loads(response_data['enemy_composition'])

        if response_data['results']:
            response_data['results'] = json.loads(response_data['results'])

        return response_data, 200

    @staticmethod
    def get_town_battles(user, town_uuid):
        """Get all battles for a town"""
        town = Town.query.filter_by(uuid=town_uuid, user_id=user.id).first()
        if not town:
            return {'message': 'Town not found.'}, 404

        battles = Battle.query.filter_by(town_id=town.id).all()

        # Format the response
        response_data = []
        for battle in battles:
            battle_data = battle.to_dict()

            # Parse JSON strings to objects
            if battle_data['enemy_composition']:
                battle_data['enemy_composition'] = json.loads(battle_data['enemy_composition'])

            if battle_data['results']:
                battle_data['results'] = json.loads(battle_data['results'])

            response_data.append(battle_data)

        return response_data, 200