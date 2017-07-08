from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    
    return render(request, "login/index.html", {"form":form})

def logout_view(request):
    return render(request, "login/index.html", {})