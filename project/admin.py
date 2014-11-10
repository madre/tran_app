# coding=utf-8
from django.contrib import admin

# Register your models here.

from models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'tran_url', 'origin_url', 'completed', 'join_users', 'picture')
    list_display_links = ['title']
    date_hierarchy = 'created'
    search_fields = ['title', ]

    def join_users(self, obj):
        return "<br>".join([each.userprofile.nickname for each in obj.user.all()])

    join_users.short_description = "参与用户"
    join_users.allow_tags = True

    def picture(self, obj):
        if obj.img:
            return '<img src="%s"; height="188px";/>' % obj.img.url
        return ''
    picture.short_description = '项目图片'
    picture.allow_tags = True

admin.site.register(Project, ProjectAdmin)