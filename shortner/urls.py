from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name='index'),
    path("submit",views.submit, name='submit'),
    path('<str:short_url>/',views.redirect,name = 'redirect'),
    # path("/<id>",views.home,name='index')

]