from django.shortcuts import render

# Create your views here.

# child class is-a parent class 

# class animal 

# makesound() 
#     print "making sounds" 

# class dog : animal 

# makesound()
#     print "woof woof"

# dog.makesound()

from django.views.generic import TemplateView 

class HelloWorld(TemplateView):
    template_name = 'test.html'