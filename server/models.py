from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, address):
        if address:
            return address
        else:
            raise ValueError('Name cannot be empty string')
    
    @validates('phone_number')
    def validate_number(self, key, address):
        if len(address) != 10:
            raise ValueError("Invalid phone number")
        return address


    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validate_content(self, key, address):
        if len(address) < 250:
            raise ValueError("Content must be 250 long")
        return address

    @validates('summary')
    def validate_summary(self, key, address):
        print(len(address))
        if len(address) >= 250:
            print(len(address))
            raise ValueError("Summary cannot be longer than 250 characters")
        return address
    
    @validates('title')
    def valite_title_bait(self, key, address):
        if "Wont' Believe" or "Secret" or "Top" or "Guess" not in address:
            raise ValueError("Not click bait-y enough")
        return address

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
