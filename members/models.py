# coding=utf-8
"""
__create_time__ = '2014/11/10'
__author__ = 'Madre'
"""
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user_id = models.OneToOneField(User)
    nickname = models.CharField("别名", max_length=500, blank=True)
    website = models.CharField("网站", max_length=500, blank=True)
    location = models.CharField("位置", max_length=500, blank=True)
    signature = models.TextField("签名", blank=True)
    avatar = models.ImageField("头相", blank=True, null=True, upload_to="avatar")

    class Meta:
        db_table = "user_profile"
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"
