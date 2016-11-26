from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from django.views.decorators.http import require_safe

from .models import Article


@require_safe
def what_to_read_next(request):
    next_page = request.GET.get('next_page', 1)
    page = Article.get_article_suggestions(next_page)
    page['articles'] = [article.as_json for article in page['articles']]
    return JsonResponse(page)


def featured_article(request):
    featured = Article.get_random_article()
    return JsonResponse(featured.as_json)


def articles(request):
    articles = Article.objects.all()
    return JsonResponse(dict(articles=[article.as_json for article in articles]))
