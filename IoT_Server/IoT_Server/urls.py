from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from MyApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^info/',views.Info),
    url(r'^postinfo/',views.postInfo),
]
