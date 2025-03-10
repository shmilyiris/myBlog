"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import show

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', show, name="home_show"),

    path('article/', include('article.urls', namespace='article')),
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    path('coding/', include('coding.urls', namespace='coding')),
    path('password-reset/', include('password_reset.urls')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('comment/', include('comment.urls', namespace='comment')),
    path('calculator/', include('calculator.urls', namespace='calculator')),
    path('todo/', include('todo.urls', namespace='todo')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
