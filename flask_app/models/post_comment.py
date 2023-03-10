from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Post_Comment:
    db_name = "apperson_blog_schema"
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.title = data['title']
        self.post_id = data['post_id']
        self.parent_id = data['parent_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#create
    @classmethod #saves new post_comment in database
    def save(cls,data):
        query = "INSERT INTO post_comment (content, title, post_id, parent_id, created_at, updated_at) VALUES (%(content)s, %(title)s, %(post_id)s, %(parent_id)s, NOW(), NOW());"
        author_id = connectToMySQL(cls.db_name).query_db(query, data)
        return author_id
#read
    @classmethod
    def get_one_with_post(cls,data):
        query = "SELECT * FROM post_comment WHERE post_id = %(post_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0])
#update
    @classmethod #edit funds
    def update(cls,data):
        query = "UPDATE post_comment SET content=%(content)s, title=%(title)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
#delete
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM post_comment WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)