# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Sith(models.Model):
    sith_names = models.CharField(max_length=50)
    planet = models.CharField(max_length=200)
    pass
    
    #message = models.OneToOneField(Msg,on_delete=models.CASCADE)   

    
    class Meta:
        ordering = ['sith_names']

    def __str__(self):
        return self.planet
   

class Questions(models.Model):
    question_text = models.CharField(max_length=1000)
    answers = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    owned_by = models.ManyToManyField(Sith,null=True)
    def __str__(self):
        return self.question_text



    

class Recruit(models.Model):
    name = models.CharField(max_length=50)
    planet = models.CharField(max_length=250)
    intergalactic_email = models.EmailField(max_length=254)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    designated_sith = models.ManyToManyField(Sith,null=True) 
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
   



