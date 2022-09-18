from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # show Todo
    path('show/', views.show, name='show'),
    # add single item
    path('add/task/', views.add_task, name='add_task'),
    # edit item
    path('finish/task/<int:id>/', views.finish_task, name='finish_task'),
    path('edit/task/<int:id>/', views.edit_task, name='edit_task'),
    path('edit/time/', views.edit_time, name="edit_time"),
    # remove item
    path('remove/task/<int:id>/', views.remove_task, name='remove_task'),
    path('remove/all/', views.remove_all, name='remove_all')

]
