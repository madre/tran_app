# coding=utf-8
"""
__create_time__ = '2014/11/10'
__author__ = 'Madre'
"""
from django.conf import settings
from django.contrib import admin
# Register your models here.

from models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nickname', 'website', 'location', 'signature', 'picture')
    list_display_links = ['nickname']
    search_fields = ['nickname', ]

    def picture(self, obj):
        if obj.avatar:
            return '<img src="%s"; height="188px";/>' % obj.avatar.url
        return ''
    picture.short_description = u'头相'
    picture.allow_tags = True

admin.site.register(UserProfile, UserProfileAdmin)