
import logging
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security import login_user, logout_user
from flask import request, session
from backend.api.models.db import db
from backend.api.models.user import user_datastore


logger = logging.getLogger(__name__)

class AuthService:
    @staticmethod
    def signup(email: str, username: str, password: str):
        if not email or not username or not password:
            logger.warning("Signup failed: missing required fields. email: %s, username: %s", email, username)
            return {'message': 'Missing required fields.'}, 400

        if user_datastore.find_user(email=email):
            logger.warning("Signup failed: Email already registered: %s", email)
            return {'message': 'Email already registered.'}, 400

        if user_datastore.find_user(username=username):
            logger.warning("Signup failed: Username already taken: %s", username)
            return {'message': 'Username already taken.'}, 400

        hashed_password = generate_password_hash(password)
        user = user_datastore.create_user(
            email=email,
            username=username,
            password=hashed_password,
            active=True
        )
        try:
            db.session.commit()
        except Exception as e:
            logger.exception("Database commit failed during signup for email: %s", email)
            return {'message': 'Internal Server Error'}, 500

        logger.info("User created successfully: email: %s, username: %s, id: %s", email, username, user.id)
        return user.to_dict(), 201

    @staticmethod
    def login(email: str, password: str):
        if not email or not password:
            logger.warning("Login failed: Missing email or password for email: %s", email)
            return {'message': 'Missing email or password.'}, 400

        user = user_datastore.find_user(email=email)

        if user and check_password_hash(user.password, password):
            login_user(user)

            user.last_login_at = user.current_login_at
            user.current_login_at = datetime.utcnow()
            user.last_login_ip = user.current_login_ip
            user.current_login_ip = request.remote_addr
            user.login_count += 1

            try:
                db.session.commit()
            except Exception as e:
                logger.exception("Database commit failed during login for email: %s", email)
                return {'message': 'Internal Server Error'}, 500

            logger.info("User logged in successfully: email: %s, IP: %s", email, request.remote_addr)
            return user.to_dict(), 200
        else:
            logger.warning("Invalid login attempt for email: %s from IP: %s", email, request.remote_addr)
            return {'message': 'Invalid email or password.'}, 401

    @staticmethod
    def get_current_user(current_user):
        if not current_user.is_authenticated:
            logger.warning("Unauthorized access attempt to get current user information.")
            return {'message': 'Unauthorized.'}, 401
        logger.info("Retrieved current user information for user: %s", current_user.email)
        return current_user.to_dict(), 200

    @staticmethod
    def logout(current_user):
        if current_user.is_authenticated:
            user_email = current_user.email
            logout_user()
            session.clear()
            logger.info("User logged out successfully: email: %s", user_email)
            return {'message': 'Logged out successfully.'}, 200
        else:
            logger.warning("Logout requested but no active session found.")
            return {'message': 'No active session.'}, 200
