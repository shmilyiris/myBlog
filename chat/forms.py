from django import forms
from .models import PublicMessage

class PublicMessagePostForm(forms.ModelForm):
    class Meta:
        model = PublicMessage
        fields = ('publisher', 'content')
