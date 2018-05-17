from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$', views.titles, name='blog_title'),
    url(r'(?P<article_id>\d)/$', views.article, name='article')
]