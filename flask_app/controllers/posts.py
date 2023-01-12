from flask import render_template, redirect, url_for, session, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.post_comment import Post_Comment

@app.route('/create', methods=['POST'])
def create():
    if 'author_id' not in session:
        return redirect ('/logout')
    data ={
        "title": request.form['title'],
        "content": request.form['content'],
        "author_id": session["author_id"]
    }
    Post.save(data)
    return redirect('/dashboard')