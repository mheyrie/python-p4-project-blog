from faker import Faker
from random import randint, choice as rc 

from app import app
from models import db, User, Tag, Post

fake = Faker()


category_list = [
    "Tech",
    "DIY",
    "Writing",
    "Fashino",
    "Food",
    "Tourism",
    "Love",
    "Life",
    "Friendship",
    "Guilt",
    "Freedom"
]

with app.app_context():
    User.query.delete()
    Post.query.delete()
    Tag.query.delete()
 

    # Generating fake data for Post model
    all_posts = []
    for value in range(15):
        p = Post(  
            image=fake.image_url(),
            title=fake.sentence(nb_words=3),
            body=fake.sentence(nb_words=30),
            
            )
        all_posts.append(p)
    db.session.add_all(all_posts)


    all_users = []
    for value in range(15):
        name = fake.name()
        email = f'{name.replace(" ", "").lower()}@gmail.com'
        u = User(
            name=name,
            email=email,
            phone_number=fake.numerify('###-###-####'),
            password=fake.password(),)
        all_users.append(u)
    db.session.add_all(all_users)
    # print(all_users)


    

    all_tags = []
    
    for value in range(15):
        t = Tag(
            category=rc(category_list),
            mins_to_read=randint(4,10),
            post=rc(all_posts),
            user=rc(all_users))
        all_tags.append(t)
    db.session.add_all(all_tags)


    



    # db.session.commit()