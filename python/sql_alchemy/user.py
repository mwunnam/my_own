#!/usr/bin/python3


from sqlalchemy import create_engine, ForeignKey, String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())


class Users(Base):
    __tablename__ = "Users"
    userID = Column("userID", String, primary_key=True, default=generate_uuid)
    firstName = Column("fistName", String)
    lastName = Column("lastName", String)
    profileName = Column("profileName", String)
    email = Column("email", String)


    def __init__(self, firstName, lastName, profileName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.profileName = profileName
        self.email = email


class Posts(Base):
    __tablename__ = "Posts"
    postId = Column("postId", String, primary_key=True, default=generate_uuid)
    userId = Column("userId", String, ForeignKey("Users.userID"))
    postContent = Column("postContent", String)

    def __init__(self, userId, postContent):
        self.userId = userId
        self.postContent = postContent


def addUser(firstName, lastName, profileName, email, session):
    email_exits = session.query(Users).filter(Users.email == email).all()
    if len(email_exits) > 0:
        print("Email address already exits, provide new one")

    profileName_exits = session.query(Users).filter(Users.profileName ==
            profileName).all()
    if len(profileName_exits) > 0:
        print("Profile Name already exits, get a new profile name")

    user = Users(firstName, lastName, profileName, email)
    session.add(user)
    session.commit()


def addPost(userId, postContent, session):
    newPost = Posts(userId, postContent)
    session.add(newPost)
    session.commit()

db = 'sqlite:///socialDB.db'
engine = create_engine(db)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

"""
addUser('Kofi', 'Lartey', 'lat', 'lat@m.com', session)
addUser('Kojo', 'Darko', 'dars', 'dars@m.com', session)
addUser('Kwame', 'Ofori', 'ofo', 'ofo@m.com', session)
"""
id_kofi = "df394c8d-0c25-4a71-8b1d-74059a7da6d"
id_kojo = "a9949735-c93e-4195-92e2-cd8623c125d"
id_kwame = "202b8a37-f264-464a-bd30-d3e607ea9024"
id_michael = "2210e633-e328-41bd-86e6-402b59634e3"



"""
addPost(id_kofi, "Take care of yourself", session)
addPost(id_kojo, "Be your self", session)
addPost(id_kofi, "Just do it?", session)
addPost(id_kofi, "Be calm", session)
"""

allPosts= session.query(Posts).filter(Posts.userId == id_kofi).all()
post_content = [p.post_content for post in allPosts]
print(post_content)

