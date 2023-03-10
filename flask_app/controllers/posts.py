from flask import render_template, redirect, url_for, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.post_comment import Post_Comment

# runs validation for new posts and creates db row in post if success
@app.route('/create', methods=['POST'])
def create():
    if 'author_id' not in session:
        flash("Must be logged in to post", "blog")
        return redirect('/')
    elif not Post.validate_post(request.form):
        return redirect('/')
    else:
        data ={
            "title": request.form['title'],
            "content": request.form['content'],
            "author_id": session["author_id"],
            "parent_id": 1
        }
        Post.save(data)
    return redirect('/')

#edit post route if owner is in session
@app.route('/edit/<int:id>')
def edit(id):
    if 'author_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    return render_template("edit.html", edit=Post.get_one(data))

#runs update to single post
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

#delete sql query
@app.route('/delete/post/<int:id>')
def delete_goal(id):
    if 'author_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Post.delete(data)
    return redirect('/')
