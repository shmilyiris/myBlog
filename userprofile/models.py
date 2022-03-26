from django.db import models
from django.contrib.auth.models import User
# 引入内置信号，在模型调用save()后发出信号
from django.db.models.signals import post_save
# 引入信号接收器的装饰器
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    # 与User模型构成一对一的关系
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 电话号码字段
    phone = models.CharField(max_length=20, blank=True)
    # 头像
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    # 个人简介
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)

'''
在后台创建并保存User时调用信号接收函数，创建Profile表
但此时管理员填写了内联Profile表会导致此表也被创建。
系统中创建了两个具有相同User的Profile表，违背了一对一原则
'''

'''
# 每当User更新后，就发送一个信号启动post_save相关的函数
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

'''

