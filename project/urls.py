# coding=utf-8
"""
__create_time__ = '11/9/14'
__author__ = 'Madre'
"""
from django.conf.urls import patterns, include, url
from project.views import ProjectView


urlpatterns = patterns('',
                       url(r'^$', ProjectView.as_view(), name="project"),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()