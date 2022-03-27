from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/userprofile/login/')
def coding(request):
    '''
    supers = User.objects.filter(is_superuser=True)
    flag = False
    for user in supers:
        if user.username == request.user.username:
            flag = True
            break
    if flag == False:
        return HttpResponse("只有超级用户有权使用该功能！")
    '''
    if not str(request.user.username):
        return HttpResponse("请先登录！")
    return render(request, 'coding/coding.html')

def show(request, id):
    if cache.has_key(id):
        headline, author, lang, code = cache.get(id);
        context = {
            'headline': headline,
            'author': author,
            'lang': lang, 
            'code': code,
        }
        return render(request, 'coding/show.html', context)
    else:
        return HttpResponse("该代码不存在！")

def generate(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        author = request.user.username
        lang = request.POST.get("lang")
        code = request.POST.get("code")
        data = [title, author, lang, code]
        num = None
        for i in range(1, 101):
            if not cache.has_key(i):
                num = i
                break

        if not num:
            print("分配地址不足")
            return HttpResponse("分配地址不足！")

        if not cache.has_key(num):
            cache.set(num, data, 3600 * 24);  # 有效期24小时

        # redirect("coding:show", id=num)
        return JsonResponse({
            'result': "success",
            'num': num,
        })
    else:
        return HttpResponse("请用POST方法获取！")

