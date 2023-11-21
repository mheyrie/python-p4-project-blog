from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Post, Tag



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
    
    elif request.method == 'POST':
        new_user = User(
            name=request.form.get('name'), 
            email=request.form.get('email'), 
            phone_number=request.form.get('phone_number'), 
            password=request.form.get('password'))
        
        db.session.add(new_user)
        db.session.commit()

        user_dict = new_user.to_dict()
        response = make_response(
            user_dict,
            201
        )

        return response

@app.route('/posts', methods=['GET'])
def posts():
    if request.method == 'GET':
        return make_response(jsonify([post.to_dict() for post in Post.query.all()]), 200)
    
@app.route('/posts/<int:id>', methods=['GET'])
def post_by_id(id):
    post = Post.query.filter(Post.id==id).first()
    
    if post == None:
        response_body = {
            "message": "Not found. Please try again."
        }
        response = make_response(response_body, 404)
        return response
    else:
        if request.method == 'GET':
            post_dict = post.to_dict()

            response = make_response(
                jsonify(post_dict),
                200
            )
            return response


@app.route('/tags', methods=['GET'])
def tags():
    if request.method == 'GET':
        return make_response(jsonify([tag.to_dict(rules=('-user', '-post'),) for tag in Tag.query.all()]), 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


