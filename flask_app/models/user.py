from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask_app.models.post import Post
from flask_app.models.post_comment import Post_Comment

class User:
    db_name = "apperson_blog_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posts = []

    @classmethod #saves new user in database
    def save(cls,data):
        query = "INSERT INTO user (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        author_id = connectToMySQL(cls.db_name).query_db(query, data)
        return author_id

    @classmethod #pulls a user from database for session
    def get_by_id(cls,data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

    @classmethod #pulls a user by email
    def get_by_email(cls,data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod #collects all users in a list
    def get_all_users(cls):
        query = "SELECT * FROM user;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_users = []
        for row in results:
            all_users.append( cls(row) )
        return all_users

    @staticmethod #validates proper information to create new user
    def validate_registration(user):
        is_valid = True
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(User.db_name).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Must enter a valid email address.","register")
            is_valid =False
        if len(user['first_name']) < 1:
            flash("You must enter a first name. ","register")
            is_valid = False
        if len(user['last_name']) < 1:
            flash("You must enter a last name. ","register")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.","register")
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Passwords do not match. Please try again.","register")
            is_valid = False
        return is_valid
