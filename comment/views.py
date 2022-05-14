from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from article.models import ArticlePost
from .forms import CommentForm
from .models import Comment
# Create your views here.

@login_required(login_url='/userprofile/login')
def post_comment(request, article_id):
    article = get_object_or_404(ArticlePost, id=article_id)

    # 处理Post请求
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            return redirect(article)
        else:
            return HttpResponse("表单内容有误，请重新填写！")
    else:
        return HttpResponse("发表评论仅接收POST请求！")


@login_required(login_url='/userprofile/login')
def delete_comment(request, comment_id, article_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return redirect("article:article_detail", id=article_id)
    else:
        return HttpResponse("仅允许POST请求")

