from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, TimeLine
from django.http import JsonResponse, HttpResponse
import markdown

# Create your views here.
md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.toc',
        ]
    )


def show(request):
    if (str(request.user.username) != 'johnson'):
        return render(request, '404.html')
    task_list = Task.objects.all()
    for task in task_list:
        task.content_md = md.convert(task.content)

    if len(TimeLine.objects.all()):
        timeline = TimeLine.objects.all()[0]
    else:
        timeline = TimeLine(content="TimeLine is Empty..")
        timeline.save()

    context = {
        'tasks': task_list,
        'timeline': timeline.content,
        'timeline_md': md.convert(timeline.content),
    }
    return render(request, 'todo.html', context)

def add_task(request):
    data = request.POST
    tmo = ''
    for i in range(int(data['tomato'])):
        tmo += '🍅'
    new_task = Task(content=data['content'], tomato=tmo)
    new_task.save()
    return JsonResponse({
        'task': new_task,
    })


def finish_task(request, id):
    task = Task.objects.get(id=id)
    task.finished = True
    task.save()

    return redirect('todo:show')

def edit_task(request, id):
    task = Task.objects.get(id=id)
    task.content = request.POST["content"]
    task.save()

    return redirect('todo:show')


def edit_time(request):
    data = request.POST
    if len(TimeLine.objects.all()):
        time = TimeLine.objects.all()[0]
        if data["content"]:
            time.content = data["content"]
    else:
        time = TimeLine(content=data["content"])
    time.save()
    return JsonResponse({
        'timeline': time.content,
        'timeline_md': md.convert(time.content),
    })


def remove_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponse("delete successful")


def remove_all(request):
    Task.objects.all().delete()
    TimeLine.objects.all().delete()
    return HttpResponse("clear successful!")
