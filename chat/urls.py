from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('chatfield/', views.chat, name='chatfield'),
]
