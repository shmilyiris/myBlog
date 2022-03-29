from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('chatfield/', views.chat, name='chatfield'),
    path('send/pub/', views.send_pub, name='send_pub'),
    path('getsrc/', views.getsrc, name='getsrc'),
]
