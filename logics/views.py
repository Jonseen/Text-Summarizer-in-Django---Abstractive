from django.http import request
from django.shortcuts import render
from .searcher import Search
from .urlloader import UrlLoader



def index(request):

    return render(request, "index.html")

def search(request):

    urlloader = UrlLoader
    queryData = urlloader.getResults(request.GET.get('search_query'))

    result = queryData['items']

    context = {
        'results':result,
        'query':request.GET.get('search_query')
    }

    return render(request, "search_result.html", context)
