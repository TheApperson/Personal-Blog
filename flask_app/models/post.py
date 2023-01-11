from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Post:
    db_name = "apperson_blog_schema"
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.author_id = data['author_id']
        self.parent_id = data['parent_id']