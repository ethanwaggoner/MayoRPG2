from flask_restx import Namespace, fields

battle_ns = Namespace('battles', description='Battle operations')

enemy_unit_model = battle_ns.model('EnemyUnit', {
    'id': fields.String(description='Enemy unit identifier'),
    'type': fields.String(description='Type of enemy'),
    'stats': fields.Raw(description='Enemy stats'),
    'position': fields.Raw(description='Grid position {x, y}')
})

battle_event_model = battle_ns.model('BattleEvent', {
    'id': fields.Integer(readOnly=True, description='Event ID'),
    'turn': fields.Integer(required=True, description='Turn number'),
    'event_type': fields.String(required=True, description='Type of event'),
    'actor_id': fields.String(required=True, description='Actor ID'),
    'target_id': fields.String(required=False, description='Target ID'),
    'data': fields.Raw(required=True, description='Event data')
})

battle_create_model = battle_ns.model('BattleCreate', {
    'town_uuid': fields.String(required=True, description='UUID of the town'),
    'difficulty_level': fields.Integer(required=True, description='Difficulty level'),
    'hero_ids': fields.List(fields.Integer, required=True, description='IDs of heroes in battle')
})

battle_model = battle_ns.model('Battle', {
    'id': fields.Integer(readOnly=True, description='Battle ID'),
    'uuid': fields.String(readOnly=True, description='Battle UUID'),
    'status': fields.String(description='Battle status'),
    'battle_seed': fields.Integer(description='Random seed for battle'),
    'enemy_composition': fields.Raw(description='Enemy units information'),
    'difficulty_level': fields.Integer(description='Battle difficulty level'),
    'enemy_scaling': fields.Float(description='Enemy stats scaling factor'),
    'created_at': fields.DateTime(description='Battle creation time'),
    'completed_at': fields.DateTime(description='Battle completion time'),
    'results': fields.Raw(description='Battle results')
})

battle_validation_model = battle_ns.model('BattleValidation', {
    'turn': fields.Integer(required=True, description='Turn number'),
    'events': fields.List(fields.Nested(battle_event_model), required=True, description='Turn events'),
    'game_state': fields.Raw(required=True, description='Current game state')
})

battle_completion_model = battle_ns.model('BattleCompletion', {
    'victory': fields.Boolean(required=True, description='Whether the battle was won'),
    'turns_taken': fields.Integer(required=True, description='Total turns taken'),
    'surviving_heroes': fields.List(fields.Integer, required=True, description='IDs of surviving heroes'),
    'final_state': fields.Raw(required=True, description='Final battle state')
})