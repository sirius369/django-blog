from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import RegistrationForm

def user_register(request):
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User(username=username, email=email, password=password)
            qs = User.objects.filter(username=username)
            if qs.exists():
                response = JsonResponse({'error' : "Username already taken"})
                return response
            else:
                user.set_password(password)
                user.save()
                login(request, user)
                response = JsonResponse({'success' : True})
            return response
        else:
            for e in form.errors.as_data():
                error = "".join(form.errors[e].as_data()[0])
            error = "".join(error)
            response = JsonResponse({'error' : error})
            return response

def auth(request):
    user_authenticated = False
    wrong_credentials = False
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user_authenticated = True
        else:
            wrong_credentials = True
    else:
        if request.user.is_authenticated:
            user_authenticated = True
        else:
            wrong_credentials = True
    print(user_authenticated)
    print(wrong_credentials)
    return JsonResponse({'logedin' : user_authenticated, 'wrong_credentials' : wrong_credentials})

def user_logout(request):
    logout(request)
    return redirect('posts:home')
