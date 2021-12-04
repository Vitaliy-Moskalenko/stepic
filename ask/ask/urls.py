from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path

urlpatterns = [
	re_path(r'^', include('qa.urls')),
    re_path(r'^admin', admin.site.urls),
]
