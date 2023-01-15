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

    @classmethod #saves a new blog post
    def save(cls,data):
        query = "INSERT INTO post (title, content, created_at, updated_at, author_id, parent_id) VALUES (%(title)s, %(content)s, NOW(), NOW(), %(author_id)s, %(parent_id)s);"
        author_id = connectToMySQL(cls.db_name).query_db(query, data)
        return author_id

    @classmethod #collects all posts in a list
    def get_all(cls):
        query = "SELECT * FROM post;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_post = []
        for row in results:
            all_post.append( cls(row) )
        return all_post
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM post WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod #edit funds
    def update(cls,data):
        query = "UPDATE post SET title=%(title)s, content=%(content)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)