
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.db.models import Count
from django.contrib import messages
import bcrypt

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def index(request):
        # User.objects.all().delete()
        # Quote.objects.all().delete()
        # Favorite.objects.all().delete()
        return render(request, "third_app/index.html")




def login(request):
        if request.method =="POST":
                login = User.objects.login(request.POST)
                if login['status']:
                        print login['data'].first_name                
                        request.session['id'] = login['data'].id
                        request.session['alias'] = login['data'].alias
                        return redirect('/homepage')
                else:
                        messages.error(request, "Email or password invalid")
        return redirect('/')        

def val(request):
        if request.method == "POST":
                res = User.objects.val(request.POST)
                if res['status']:
                        messages.success(request, "Thank You For Registering")
                        request.session['id'] = res['data'].id
                        request.session['alias'] = res['data'].alias
                        return redirect('/homepage')
                else:
                        for errors in res['data']:
                                messages.error(request, errors)
        return redirect('/')

        
        if request.method == "POST":
                Favorite.objects.get(id = request.POST['id']).delete()
                
        return redirect ('/addquote')  

def user (request, id):
    
    
    context = {
        "user" : User.objects.get(id = id)
    }

    return render(request, "third_app/user.html", context)

def homepage(request):
        if 'id' not in request.session:
                return redirect('/')
        else:
                context = {
                        "users": User.objects.all()
                }
                return render(request, "third_app/homepage.html", context)

                       
def logout(request):
        
        request.session.clear()

        return redirect ('/')    

        


