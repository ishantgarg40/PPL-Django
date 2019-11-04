from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as log_session, logout as logout_session
from django.contrib.auth.models import User
from timeline.models import Profile


def login(request):
    if request.POST.get('username'):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            log_session(request, user)
            return redirect("/timeline")
        else:
            return render(request, 'login/index.html', {'error': True})
    return render(request, 'login/index.html')


def logout(request):
    logout_session(request)
    return redirect('/account/login/')


