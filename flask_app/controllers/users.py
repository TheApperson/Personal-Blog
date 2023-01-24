from flask import render_template, redirect, url_for, session, request, jsonify
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.post_comment import Post_Comment
from flask_app.models import number_game
from flask import flash
import random

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#new user registration route
@app.route('/registration')
def registration():
    return render_template('register.html')

#existing user route
@app.route('/signin')
def signin():
    return render_template('login.html')

#runs registration validation to send to User.save
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/registration')
    data ={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['author_id'] = id
    return redirect('/')

#login and redirect to dashboard with session
@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/signin')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/signin')
    session['author_id'] = user.id
    return redirect('/')

#dashboard accessible to guests and users.
@app.route('/')
def dashboard():
    if 'author_id' not in session:
        return render_template("dashboard.html", users=User.guest(), posts=Post.get_all(), bloggers=User.get_all_users())
    data ={
        'id': session['author_id']
    }
    return render_template("dashboard.html", users=User.get_by_id(data), posts=Post.get_all(), bloggers=User.get_all_users())

#logout with dashboard redirect
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

#dev playground, test page for minor project clones
@app.route('/colorful')
def colorful():
    return render_template('index.html')

def build_list(x):
    result = []
    for i in range(x+1):
        if i == 0:
            pass
        else:
            result.append(i)
    return result

@app.route('/guesser', methods=['GET', 'POST'])
def guesser():
    build_list(1000)
    if request.method == 'POST':
        last_guess = 0
        last_answer = 0
        remaining_guess = 0
        guess = request.form['guess']
        if 'answer' not in session:
            session['answer'] = random.randint(1, 1000)
            session['guess_min'] = 1
            session['guess_max'] = 1000
            session['turns_left'] = 15
        else:
            if int(session['turns_left']) == 1:
                last_answer=session['answer']
                flash(f"No more guesses.. you lose! :( The answer was {last_answer}", "guess")
                session.pop('answer', None)
            elif guess == "":
                flash("Enter a guess!","guess")
            elif int(guess) < int(session['guess_min']) or int(guess) > int(session['guess_max']):
                flash("Invalid guess","guess")
            elif int(guess) > session['answer']:
                last_guess = guess
                session['turns_left'] -= 1
                session['guess_max'] = guess
            elif int(guess) < session['answer']:
                last_guess = guess
                session['turns_left'] -= 1
                session['guess_min'] = guess
            else:
                remaining_guess = session['turns_left']
                flash(f"You win! With {remaining_guess} guesses left.", "guess")
                session.pop('answer', None)
        return render_template('guesser.html', answer=session.get('answer'), guess_min=session.get('guess_min'),
        guess_max=session.get('guess_max'), guess = last_guess, turns_left=session.get('turns_left'), last_answer=last_answer, remaining_guess=remaining_guess)
    return render_template('guesser.html')