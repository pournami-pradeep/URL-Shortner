from .models import Urls
from django import forms

class CreateShortURL(forms.ModelForm):
    big_url = forms.CharField(label="big_url", max_length=100)

    class Meta:
        model = Urls
        fields = ['big_url']
