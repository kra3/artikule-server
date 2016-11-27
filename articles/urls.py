from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^articles/(?P<id>[0-9]+)/$', views.article, name='article'),
    url(r'^articles/suggest/$', views.what_to_read_next, name='article_suggestions'),
    url(r'^articles/featured/$', views.featured_article, name='random_article'),
]
