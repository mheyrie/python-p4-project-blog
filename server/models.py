from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, CheckConstraint
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


#*********************************************************************************#

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    serialize_rules = ('-tags.post', '-tags.user',)

    id = db.Column(db.Integer, primary_key=True)
    image= db.Column(db.String)
    title = db.Column(db.String(100))
    body = db.Column(db.String(300))

    tags =db.relationship('Tag', backref='post')
    
    def __repr__(self):
        return f'<Post {self.title}, {self.body} >'
    
#*********************************************************************************#
class Tag(db.Model, SerializerMixin):
    __tablename__ = 'tags'

    serialize_rules = ('-post.tags', 'user.tags', '-post_id')

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100))
    mins_to_read = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

       
    def __repr__(self):
        return f'<Tag Category {self.category}, {self.mins_to_read} mins to read>'
    
    
#*********************************************************************************#

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-tags.user',)


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String, CheckConstraint('len(phone_number) == 12'), nullable=False)
    password = db.Column(db.String(256), nullable=False)

    tags =db.relationship('Tag', backref='user')

    def __repr__(self):
        return f'<User {self.name} {self.email} {self.phone_number}>'

   
    #Email validation
    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError("Enter a correct email address")
        return address




