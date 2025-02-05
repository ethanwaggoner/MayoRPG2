from flask_restx import fields, Namespace

auth = Namespace('auth', description='Authentication operations')

signup_model = auth.model('Signup', {
    'email': fields.String(required=True, description='User email', pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$', min_length=5, max_length=255),
    'username': fields.String(required=True, description='Username', min_length=3, max_length=50),
    'password': fields.String(required=True, description='Password', min_length=8, max_length=128),
})

login_model = auth.model('Login', {
    'email': fields.String(required=True, description='User email', pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$', min_length=5, max_length=255),
    'password': fields.String(required=True, description='Password', min_length=8, max_length=128),
})

user_model = auth.model('User', {
    'id': fields.Integer(description='User ID'),
    'fs_uniquifier': fields.String(description='Unique identifier'),
    'username': fields.String(description='Username'),
    'email': fields.String(description='User email'),
    'active': fields.Boolean(description='Active status'),
    'last_login': fields.DateTime(description='Last login time'),
    'current_login': fields.DateTime(description='Current login time'),
    'last_login_ip': fields.String(description='Last login IP'),
    'current_login_ip': fields.String(description='Current login IP'),
    'login_count': fields.Integer(description='Login count'),
    'roles': fields.List(fields.String, description='User roles'),
})

message_model = auth.model('Message', {
    'message': fields.String(description='Response message'),
})
