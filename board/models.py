from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class user(models.Model) :
    userid=models.CharField(max_length=50,unique=True)
    pw=models.CharField(max_length=300)
    signdate=models.DateTimeField()
    expiredate=models.DateTimeField()
    name=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    auth=models.CharField(max_length=50)


class board(models.Model) :
    boardid=models.IntegerField(primary_key=True)
    boardname=models.CharField(max_length=50)
    cre_date=models.DateTimeField()

class boardcontent(models.Model) :
    boardcontentid=models.IntegerField(primary_key=True)
    boardid=ForeignKey('board',related_name='category',on_delete=CASCADE)
    cre_date=models.DateTimeField()
    userid=models.ForeignKey('user',related_name='posted_name',on_delete=CASCADE)
    hit=models.IntegerField()
    isnotice=models.BooleanField()
    content=models.TextField()

class bookmark(models.Model) :
    boardcontentid=models.ForeignKey('boardcontent',related_name='bookmark_on',on_delete=CASCADE)
    userid=models.ForeignKey('user',related_name='bookmarked_by',on_delete=CASCADE)

class like(models.Model) :
    boardcontentid=models.ForeignKey('boardcontent',related_name='like_or_dislike_this',on_delete=CASCADE)
    cipherid=models.ForeignKey('user',related_name='who_like',on_delete=CASCADE)
    like=models.BooleanField()

class chatroom(models.Model) :
    chatroomid=models.IntegerField(primary_key=True)
    chatroomname=models.CharField(max_length=50)
    cre_date=models.DateTimeField()


class chatusers(models.Model) :
    chatroomid=models.ForeignKey('chatroom',related_name='where_in',on_delete=CASCADE)
    chatroomname=models.CharField(max_length=25)
    cre_date=models.DateTimeField()

class chat(models.Model) :
    chatid=IntegerField(primary_key=True)
    chatroomid=models.ForeignKey('chatroom',related_name='where_talk',on_delete=RESTRICT)
    userid=models.ForeignKey('user',related_name='who_chatted',on_delete=RESTRICT)

class reply(models.Model) :
    replyid=models.IntegerField(primary_key=True)
    boardcontentid=ForeignKey('boardcontent',related_name='where_replied',on_delete=CASCADE)
    userid=models.ForeignKey('user',related_name='who_id_replied',on_delete=CASCADE)
    cre_date=models.DateTimeField()
    reply=models.TextField()

class rereply(models.Model) :
    rereplyid=models.IntegerField(primary_key=True)
    replyid=ForeignKey('reply',related_name='where_rereplied',on_delete=CASCADE)
    cre_date=models.DateTimeField()
    userid=models.ForeignKey('user',related_name='who_name_rereplied',on_delete=CASCADE)
    rereply=models.TextField()

    


