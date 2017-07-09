from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm

def login_view(request):
    if request.user.is_authenticated:
       return redirect('/todo/')
    
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/todo/')
    return render(request, "login/login.html", {"form":form})

def logout_view(request):
    logout(request)
    return redirect('/login/')