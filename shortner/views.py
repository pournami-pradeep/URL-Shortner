import random
import string

from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateShortURL
from .models import Urls


def home(request):   
    return render(request, "shortner/home.html")


def shorten():
    random_letters = list(string.ascii_letters)
    while True:
        short = ''.join(random.choices(random_letters,k = 6))
        if not Urls.objects.filter(short_url = short).exists():
            break
    return short


def submit(request):
    domain = request.scheme +"://" + request.get_host() + '/'
    form = CreateShortURL(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        original_url = form.cleaned_data['big_url']
        short_url = shorten()
        Urls.objects.create(big_url = original_url,
                            short_url = short_url)
            
        return render(request,'shortner/shortner.html',{"short_url": domain + short_url+'/'})
    if not form.is_valid():
        # print("OKKKKK")
        return render(request, 'shortner/shortner.html',{"invalid_case" : "Invalid URL"})
    return render(request, 'shortner/home.html')


def redirect(request, short_url):
    try:
        big_url = Urls.objects.get(short_url = short_url).big_url
    except:
        return HttpResponse("Page not found")
    return HttpResponseRedirect(big_url)
    



