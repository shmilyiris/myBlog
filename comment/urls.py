from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    # 发表评论
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
    # 删除评论
    path('delete-comment/<int:comment_id>/<int:article_id>/', views.delete_comment, name='delete_comment'),
]
