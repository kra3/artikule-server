from django.shortcuts import render


def index(request):
    from django.http import HttpResponse
    return HttpResponse("Hello")


def article(request, id):
    # show the article
    return
