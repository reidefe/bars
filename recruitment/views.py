# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

from random import seed, randint

from .models import Questions, Sith, Recruit

from django.template import loader

from django import forms

from django.forms import ModelForm

#from django.views.generic import ListView, CreateView, 

from django.core.mail import send_mass_mail, send_mail



def Home(request):    
    return render(request, 'recruitment/Home.html')
    


class enrollment_form(ModelForm):
    class Meta:
        model = Recruit
        fields = ['name', 'planet','intergalactic_email','age']   
          

def enrollment(request):
    form = enrollment_form(request.POST)
    if request.method == 'POST':
        if form.is_valid():             
            f = form.save()            
            sith_to_be_assigned = form.cleaned_data['planet']  
            s = Sith.objects.get(planet=sith_to_be_assigned)
            sith = f.designated_sith.add(s)            
            form.save()                  
              
            return HttpResponseRedirect('Questions/') 
   
    context = {'form': form}    
    return render(request, 'recruitment/enrollment.html', context)   




class question_form(ModelForm):
    class Meta:
        model = Questions
        fields = [ 'answers']         

seed(1)

q = Questions.objects.all()[:2]

def question(request):  
    siths  = Sith.objects.all()
    
    if request.method == 'POST':
        for _ in q:
            form = question_form(request.POST)               

        if form.is_valid():
            form.save()           
                        



        return HttpResponseRedirect('await/')    
    else:
        form = question_form()  
    context = {'form': form,  'q':q }          
    return render(request, 'recruitment/questions.html', context,)


class sith_details(ModelForm):
    class Meta:
        model = Sith
        fields  = ['sith_names']
    # selected widget with all sith lords 
    # then try to find their given students based on planet location
    # show students scores
    # then send an intergalactic email if the scores are good enough for the sith

def get_sith(request): 
    r = None
    s = None
    sith = Sith.objects.all()
    form = sith_details(request.GET)
    if request.method  == 'GET' :
        if form.is_valid():
            sith_name = form.cleaned_data['sith_names']
            print(sith_name)
            s = Sith.objects.get(sith_names=sith_name)
            r = Recruit.objects.get(designated_sith=s)    
    context = {'form':form,'sith':sith, 'r': r, 's':s}
    return render(request, 'recruitment/Sith.html', context )


def await_reply(request):
    return render(request,'recruitment/await.html') 


def show_recruits(request):
    
    return render(request, 'recruitment/show_recruit.html',) 
