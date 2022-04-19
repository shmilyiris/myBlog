from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost, ArticleColumn
from .forms import ArticlePostForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from comment.models import Comment
from django.db.models import Q
import markdown

# Create your views here.

def article_list(request):
    # 取出所有博客文章
    search = request.GET.get('search')
    order = request.GET.get('order')
    if search:
        if order == 'total_views':
            article_list = ArticlePost.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            ).order_by('-total_views')
        else:
            article_list = ArticlePost.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            )
    else:
        search = ''
        if request.GET.get('order') == 'total_views':
            article_list = ArticlePost.objects.all().order_by('-total_views')
        else:
            article_list = ArticlePost.objects.all()
    # 每页显示3篇文章
    paginator = Paginator(article_list, 5)
    # 获取url中的页码，并获取对应文章
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    # 需要传给模板的对象
    context = { 'articles':articles, 'order': order, 'search': search }

    return render(request, 'article/list.html', context)

def article_detail(request, id):
    # 取出对应id的文章
    article = ArticlePost.objects.get(id=id)

    # 浏览量+1
    article.total_views += 1
    article.save(update_fields=['total_views'])

    # 将markdown语法渲染成html样式
    md = markdown.Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc', # 目录扩展
            ]
    )

    article.body = md.convert(article.body)
    comments = Comment.objects.filter(article=id)
    # 需要传递给模板的对象
    context = {'article':article, 'toc': md.toc, 'comments': comments}
    return render(request, 'article/detail.html', context)

# 写入文章的视图
@login_required(login_url='/userprofile/login/')
def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id) # 指定文章作者为当前登录用户
            if request.POST['column'] != 'none':
                new_article.column = ArticleColumn.objects.get(id=request.POST['column'])
            new_article.save()
            # 保存tags的多对多关系
            article_post_form.save_m2m()
            return redirect("article:article_list")
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        article_post_form = ArticlePostForm()
        columns = ArticleColumn.objects.all()
        context = { 'article_post_form': article_post_form, 'columns': columns}
        return render(request, 'article/create.html', context)

# 安全删除文章的视图
def article_safe_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        if str(article.author) != request.user.username:
            return HttpResponse("你不是本人，无权删除文章！")
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许Post请求")

# 修改文章的视图
def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    if str(article.author) != request.user.username:
        return HttpResponse("你不是本人，无权更改文章！")

    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)

        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.introduction = request.POST['introduction']
            if request.POST['column'] != 'none':
                article.column = ArticleColumn.objects.get(id=request.POST['column'])
            else:
                article.column = None
            article.save()
            return redirect("article:article_detail", id=id)
        else:
            return HttpResponse("表单数据有误，请重新填写。")
    else:
        article_post_form = ArticlePostForm()
        columns = ArticleColumn.objects.all()
        context = {
            'article': article, # 为了提取更改前的内容
            'article_post_form': article_post_form,
            'columns': columns,
        }
        return render(request, 'article/update.html', context)



