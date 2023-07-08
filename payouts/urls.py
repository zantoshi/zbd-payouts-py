from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('withdrawal', views.withdraw, name='withdrawal'),
    path('pay', views.pay, name='pay'),
    path('callback', csrf_exempt(views.callback), name="callback"),
]
