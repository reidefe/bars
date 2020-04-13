from django.contrib import admin
from django.urls import path, include
from .views import await_reply,enrollment,recruit_list, Home, question, question_form, sith_details, recruit_details


urlpatterns = [
    path('home/', Home, name='index'),
    path('sith/Home/', Home, name='Home'),
    path('show_recruit/', recruit_list, name='show_recruit'),
    path('sith/', sith_details.as_view(), name='sith'),
    path('serve_us/Questions/', question, name='questions'),
    path('serve_us/', enrollment, name='serve_us'),
    path('await/', await_reply, name='await'),
    path('sith/recruit_details/', recruit_details.as_view(), name='recruit_details'),
    path('recruit_details/', recruit_details.as_view(), name='recruit_details'),
    path('serve_us/Questions/await/', await_reply, name='questions'),
    
]
