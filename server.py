from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import posts

if __name__=="__main__":
    app.run(port=3308,debug=True)
    print('running')

"""if __name__ == "__main__":
    app.run()"""