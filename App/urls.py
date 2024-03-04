from django.urls import path, include
from App.views import *

urlpatterns = [
    path('', homePage, name='homepage'),
    path('trial/',  trialPage, name="trial"),
]
