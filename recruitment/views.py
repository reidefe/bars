# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

from random import seed, randint

from .models import Questions, Sith, Recruit

from django.template import loader

from django import forms

from django.views import View

from django.forms import ModelForm, ModelChoiceField, MultipleChoiceField

from django.views.generic.edit import FormView

from django.core.mail import send_mail


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
x = randint(0,5)
    

q = Questions.objects.all()[:x]

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


class sith_details1(ModelForm):   
    class Meta:
        model = Sith
        fields = ['sith_names']


def get_sith(request):
    if request.method == 'POST' :
        form = sith_details1()
        if form.is_valid():
            sith_name = form.cleaned_data['sith_names']           
            s = Recruit.object.get(designated_sith=sith_name)
            return redirect('recruit_details/',  s, sith_name) 
            
        else:
            form = sith_details()  

        context = {'form': form, }     

        return render(request, 'recruitment/Sith.html', context,) 


  

class sith_details(FormView):
    template_name = 'recruitment/Sith.html'
    form_class = sith_details1
    
    def form_valid(self, form):           
        sith_name = form.cleaned_data['sith_names']       
        s = Sith.objects.filter(sith_names=sith_name) 
        print(s)            
        sith_recruits = Recruit.objects.filter(planet__startswith=[s]) 
        print([sith_recruits]) 
        for r in sith_recruits:
            print(r)            
            recruit_mail = r.intergalactic_email        
            send_mail('Notification from the Sith order','We suggest that future notifications be sent through intergalactic communication instead of email, but this is not known exactly','reidefe@gmail.com', [recruit_mail] )        
            
        return redirect('Home/' )         
    





class list_of_recruits_in_sith(ModelForm):
    class Meta:
        model = Sith
        fields = ['sith_names']


def recruit_list(request): 
    form = list_of_recruits_in_sith(request.POST) 
    if request.method =='POST' :
        if form.is_valid():
            sith_name = form.cleaned_data['sith_names'] 
            s = Sith.objects.filter(sith_names=sith_name) 
            r = Recruit.objects.filter(designated_sith=s) 
            print([r])    
            
            context = { 'form':form, 'r': r, 's':s}
            return render(request,'recruitment/show_recruitment.html', context)         
    



























class recruit_details(View):
    def get(self, request, s, sith_name):
        n = Recruit.objects.filter(designated_sith=s)
        #score =    
        return render(request,'recruitment/show_recruit.html', {'n':n}) 



   
def await_reply(request):
    return render(request,'recruitment/await.html') 

 
class email(forms.Form):
    a = forms.CharField()
    
'''
def send_email(request):
    form = email()
    if request.method == 'POST':
        form = email(request.POST)
        if form.is_valid:
            s = Sith.objects.all()
            r = Recruit.objects.all()
            fo
            r_in_ s = s.recruit_set.filter(designated_sith=r.name)
            r_mail = 
            notes = form.cleaned_data
            send_mail('Notification from the Sith order',notes,'reidefe@gmail.com',  )
    
             
     '''   






    