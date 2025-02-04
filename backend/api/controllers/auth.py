import logging
from flask import request
from flask_restx import Namespace, Resource
from flask_security import current_user, login_required
from backend.api.schemas.auth import (
    auth,
    signup_model,
    login_model,
    user_model,
    message_model
)
from backend.api.services.auth import AuthService
from backend.api.limiter import limiter

logger = logging.getLogger(__name__)

auth_ns = auth

@auth_ns.route('/signup')
class SignupController(Resource):
    @auth_ns.expect(signup_model)
    @auth_ns.response(201, 'User created successfully.', user_model)
    @auth_ns.response(400, 'Validation Error', message_model)
    @limiter.limit("6/minute")
    def post(self):
        data = request.get_json()
        email = data.get('email')
        username = data.get('username')
        logger.info("Received signup request for email: %s, username: %s", email, username)
        response = AuthService.signup(email, username, data.get('password'))
        logger.info("Signup response for email %s: %s", email, response[1])
        return response


@auth_ns.route('/login')
class LoginController(Resource):
    @auth_ns.expect(login_model)
    @auth_ns.response(200, 'Login successful.', user_model)
    @auth_ns.response(400, 'Validation Error', message_model)
    @auth_ns.response(401, 'Invalid credentials.', message_model)
    @limiter.limit("6/minute")
    def post(self):
        data = request.get_json()
        email = data.get('email')
        logger.info("Received login request for email: %s from IP: %s", email, request.remote_addr)
        response = AuthService.login(email, data.get('password'))
        if response[1] == 200:
            logger.info("Login successful for email: %s", email)
        else:
            logger.warning("Login failed for email: %s with status code: %s", email, response[1])
        return response


@auth_ns.route('/current_user')
class CurrentUserController(Resource):
    @login_required
    @auth_ns.response(200, 'Success', user_model)
    @auth_ns.response(401, 'Unauthorized', message_model)
    @limiter.limit("6/minute")
    def get(self):
        logger.info("Received request for current user information")
        response = AuthService.get_current_user(current_user)
        if response[1] == 401:
            logger.warning("Unauthorized access to current user endpoint")
        return response


@auth_ns.route('/logout')
class LogoutController(Resource):
    @login_required
    @auth_ns.response(200, 'Logout successful.', message_model)
    def post(self):
        logger.info("Received logout request for user: %s", getattr(current_user, 'email', 'Unknown'))
        response = AuthService.logout(current_user)
        logger.info("Logout response: %s", response[1])
        return response
