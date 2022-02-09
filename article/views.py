from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost
from .forms import ArticlePostForm
from django.contrib.auth.models import User
import markdown

# Create your views here.

def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传给模板的对象
    context = {'articles':articles}
    return render(request, 'article/list.html', context)

def article_detail(request, id):
    # 取出对应id的文章
    article = ArticlePost.objects.get(id=id)

    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body, 
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
    # 需要传递给模板的对象
    context = {'article':article}
    return render(request, 'article/detail.html', context)

# 写入文章的视图
def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=1)
            new_article.save()
            return redirect("article:article_list")
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        article_post_form = ArticlePostForm()
        context = { 'article_post_form': article_post_form }
        return render(request, 'article/create.html', context)

# 安全删除文章的视图
def article_safe_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许Post请求");


