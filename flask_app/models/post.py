from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Post:
    db_name = "apperson_blog_schema"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.author_id = data['author_id']
        self.parent_id = data['parent_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO post (title, content, created_at, updated_at, author_id, parent_id) VALUES (%(title)s, %(content)s, NOW(), NOW(), %(author_id)s, %(parent_id)s);"
        author_id = connectToMySQL(cls.db_name).query_db(query, data)
        return author_id