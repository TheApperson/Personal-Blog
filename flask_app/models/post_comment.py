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

#read

#update

#delete