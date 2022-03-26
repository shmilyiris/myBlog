import sys
from django.conf import settings
from django.shortcuts import render
# sys.path.append(settings.USERPROFILE_ROOT)
# from forms import UserLoginForm, ProfileForm
# from models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/userprofile/login/')
def chat(request):
    # user = User.objects.get(id=id)
    '''
    if request.method == 'GET':
        profile_form = ProfileForm()
        context = {
            'profile_form': profile_form,
        }
        '''
    return render(request, 'chat/chat.html')
