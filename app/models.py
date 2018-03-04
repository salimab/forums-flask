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
import datetime
class Member() :

    def __init__(self,name,age):
        self.id = 0
        self.name = name
        self.age = age
        self.posts = []

    def __str__(self):
        return "Name: {}, Age: {}".format(self.name, self.age)
class Post() :

    def __init__(self,title,topic,member_id = 0 ):
        self.id = 0
        self.title = title
        self.topic = topic
        self.member_id = member_id
        self.date = datetime.datetime.now()

    def __str__(self):
        return "Title: {}, Content: {}".format(self.title, self.topic)








