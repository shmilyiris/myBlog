from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def coding(request):
    supers = User.objects.filter(is_superuser=True)
    flag = False
    for user in supers:
        if user.username == request.user.username:
            flag = True
            break
    if flag == False:
        return HttpResponse("只有超级用户有权使用该功能！")
    return render(request, 'coding/coding.html')
