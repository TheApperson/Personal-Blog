from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import posts

if __name__=="__main__":
    app.run(port=3000, debug=True)
    print('running')