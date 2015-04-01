from flask import Flask
from flask.ext.misaka import Misaka
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config['SECRET_KEY'] = 'blogme'
app.config['MONGODB_SETTINGS'] = {
    'db': 'flask-blog',
    'host': '127.0.0.1',
    'port': 27017
}
md = Misaka(app)
db = MongoEngine(app)


def register_blueprints(app):
    from blog.views import posts
    app.register_blueprint(posts)


register_blueprints(app)


if __name__ == '__main__':
    app.run()
