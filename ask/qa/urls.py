from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('^$',           views.test),
    re_path('^login/.*$',   views.test),
    re_path('^signup/.*$',  views.test),
    re_path('^question/(?P<id>[0-9]+)/$', views.test),
    re_path('^ask/.*$',     views.test),
    re_path('^popular/.*$', views.test),
    re_path('^new/.*$',     views.test),
]
