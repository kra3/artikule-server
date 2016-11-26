from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^suggest_articles/$', views.what_to_read_next, name='article_suggestions'),
    url(r'^featured_article/$', views.featured_article, name='random_article'),
    url(r'^articles/$', views.articles, name='articles'),
]
