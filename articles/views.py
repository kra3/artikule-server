from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_safe

from .models import Article


@require_safe
def what_to_read_next(request):
    next_page = request.GET.get('next_page', '1')
    next_page = int(next_page) if next_page.isdigit() else 1
    page = Article.get_article_suggestions(next_page)
    page['articles'] = [article.as_json for article in page['articles']]
    return JsonResponse(page)


@require_safe
def featured_article(request):
    featured = Article.get_random_article()
    return JsonResponse(featured.as_json)


@require_safe
def articles(request):
    articles = Article.objects.all()
    return JsonResponse(dict(articles=[article.as_json for article in articles]))


@require_safe
def article(request, id):
    article = get_object_or_404(Article, id=id)
    return JsonResponse(article.as_json)
