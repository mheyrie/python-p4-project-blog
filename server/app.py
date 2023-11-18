from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Post



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)


db.init_app(app)

@app.route('/')
def home():
    return '<h1>Welcome to my Blog</h1>'

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return make_response(jsonify([user.to_dict(rules=('-tags','-password',)) for user in User.query.all()]), 200)
    
    if request.method == 'POST':
        data = request.get_json()
        user = User(name=data.get('name'), email=data.get('email'), phone_number=data.get('phone_number'), password=data.get('password'))
        db.session.add(user)
        db.session.commit()
        return make_response(
            jsonify(
                {'id': user.id, 'name': user.name, 'email': user.email, 'phone_number': user.phone_number, 'password': user.password}
            )
        )

@app.route('/posts', methods=['GET'])
def posts():
    if request.method == 'GET':
        return make_response(jsonify([post.to_dict() for post in Post.query.all()]), 200)



if __name__ == '__main__':
    app.run(port=5555, debug=True)


