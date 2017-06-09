from django.shortcuts import render, HttpResponse
from firstapp.models import People, Article
from django.template import Context, Template

# Create your views here.
def index(request):
    print(request)
    print('==='*30)
    print(dir(request))
    print('==='*30)
    print(type(request))
    queryset = request.GET.get('tag')
    if queryset:
        article_list = Article.objects.filter(tag=queryset)
    else:
        article_list = Article.objects.all()
    context = {}
    article_list = Article.objects.all()
    context['article_list'] = article_list
    index_page = render(request, 'first_web_2.html', context)
    return index_page