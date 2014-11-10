#coding=utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(u"标题", max_length=500)
    desc = models.TextField(u"描述")
    tran_url = models.CharField(u"翻译地址", max_length=500, blank=True)
    origin_url = models.CharField(u"源站地址", max_length=500, blank=True)
    img = models.ImageField(u"项目图片", blank=True, null=True, upload_to="project")
    completed = models.CharField(u"完成情况", max_length=36, help_text=u"填写百比分")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(User)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'project'
        verbose_name = '翻译项目'
        verbose_name_plural = verbose_name