from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost

# Create your views here.

def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传给模板的对象
    context = {'articles':articles}
    return render(request, 'article/list.html', context)
