from flask import render_template, redirect, url_for, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.post_comment import Post_Comment

@app.route('/create', methods=['POST'])
def create():
    if 'author_id' not in session:
        flash("Must be logged in to post", "blog")
        return redirect('/')
    if len(request.form['title']) < 1:
        flash("You must enter a title. ","blog")
    if len(request.form['title']) > 150:
        flash("Title is too long. ","blog")
    if len(request.form['content']) < 1:
        flash("You must add content. ","blog")
    if len(request.form['content']) < 20:
        flash("Content is too short. ","blog")
    else:
        data ={
            "title": request.form['title'],
            "content": request.form['content'],
            "author_id": session["author_id"],
            "parent_id": 1
        }
        Post.save(data)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    if 'author_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    return render_template("edit.html", edit=Post.get_one(data))

@app.route('/update/post',methods=['POST'])
def update_post():
    if 'author_id' not in session:
        return redirect('/logout')
    data = {
        "id": request.form["id"],
        "title": request.form["title"],
        "content": request.form["content"]
    }
    print(data)
    Post.update(data)
    return redirect('/')
