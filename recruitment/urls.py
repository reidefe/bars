from django.contrib import admin
from django.urls import path, include
from .views import get_sith,await_reply, enrollment, Home, question, question_form


urlpatterns = [
    path('home/', Home, name='index'),
    path('sith/', get_sith, name='sith'),
    path('serve_us/Questions/', question, name='questions'),
    path('serve_us/', enrollment, name='serve_us'),
    path('await/', await_reply, name='await'),
     path('serve_us/Questions/await/', await_reply, name='questions'),
    
]
