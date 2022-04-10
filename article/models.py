from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class ArticlePost(models.Model):
    # 文章作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 文章标题
    title = models.CharField(max_length=100)
    # 文章简介
    introduction = models.CharField(max_length=100, default="这是一篇文章..")
    # 文章正文
    body = models.TextField()
    # 文章创建时间
    created = models.DateTimeField(default=timezone.now)
    # 文章更新时间
    updated = models.DateTimeField(auto_now=True)
    # 文章浏览量
    total_views = models.PositiveIntegerField(default=0)


    # 内部类，用于给model定义元数据
    class Meta:
        # ordering指定模型返回数据的排列顺序
        ordering = ('-created', )

    def __str__(self):
        return self.title

