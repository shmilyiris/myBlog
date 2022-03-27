from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from userprofile.forms import UserLoginForm, ProfileForm
from userprofile.models import Profile
from .forms import PublicMessagePostForm
from .models import PublicMessage
import time
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/userprofile/login/')
def chat(request):
    if str(request.user.username):
        if request.method == 'GET':
            user = User.objects.get(username=str(request.user.username))
            profile = Profile.objects.get(user_id=request.user.id)
            profile_form = ProfileForm()
            # 获取publish的history
            histories = []
            for item in PublicMessage.objects.all():
                histories.append(item.content)
            context = {
                'histories': histories,
                'profile_form': profile_form,
                'profile': profile,
                'user': user,
            }
            return render(request, 'chat/chat.html', context)
    else:
        return HttpResponse("请先登录！")

def send_pub(request):
    if request.method == 'POST':
        curtime = time.strftime('%m/%d %H:%M')
        data = request.POST
        content = "[" + curtime + "] " + data['content']
        # 检查公开聊天记录是否超过100条
        if len(PublicMessage.objects.all()) > 99:
            PublicMessage.objects.all().first().delete() # 删除最早一条
        public_message_form = PublicMessagePostForm()
        new_message = public_message_form.save(commit=False)
        new_message.publisher = User.objects.get(id=request.user.id)
        new_message.content = content
        new_message.save()
        return JsonResponse({
            'content': content,
        })
    else:
        return HttpResponse("请用POST方法请求数据")


