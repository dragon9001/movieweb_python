#  -*- coding: UTF-8 -*-
from django.db import models
# Create your models here.

''' 视频 URL 存数据库 '''


class Movie(models.Model):
    movie = models.CharField(max_length=100)

    def __str__(self):
        return self.movie


class Video(models.Model):
    v_id = models.IntegerField()
    title = models.CharField(max_length=100)
    video_url = models.CharField(max_length=150)
    image_url = models.CharField(max_length=150)
    v_type = models.CharField(max_length=50)

    def __str__(self):
        return 'v_id: %d | title: %s | video_url: %s | image_url: %s | v_type: %s ' % (self.v_id, self.title, self.video_url, self.image_url, self.v_type)


''' 用户名 存数据库 '''


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.IntegerField()

    def __str__(self):
        return '%s | %s' % (self.username, self.password)

''' 用户评论 存数据库 '''


class UserComment(models.Model):
    comment_username = models.CharField(max_length=20)
    user_comment = models.CharField(max_length=300)
    comment_time = models.CharField(max_length=40)

    def __str__(self):
        return "%s : %s | %s" % (self.comment_username, self.user_comment, self.comment_time)
''' 用户支付 存数据库 '''


class MoviePay(models.Model):
    pay_username = models.CharField(max_length=20)
    movie_id = models.IntegerField()
    movie_pay = models.IntegerField()

    def __str__(self):
        return "user: %s / movie_id: %d / pay: %d" % (self.pay_username, self.movie_id, self.movie_pay)
