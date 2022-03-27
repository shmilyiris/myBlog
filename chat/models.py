from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PublicMessage(models.Model):
    # 发布者
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    # 发布内容
    content = models.TextField()

    def __str__(self):
        return self.content
