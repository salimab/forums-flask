#-------------------------------------------------------------------------------
# Name:        Models
# Purpose:
#
# Author:      user
#
# Created:     10/02/2018
# Copyright:   (c) user 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from app import db

class Member(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    posts = db.relationship("Post", backref = "members")

    def __repr__(self):
        return "Id: {self.id}, Name: {self.name}, Age: {self.age}"

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "posts": self.posts,
        }


class Post(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(800))
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"))

    def __repr__(self):
        return "Title: {self.title}, Content: {self.content}"

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "member_id": self.member_id,
        }