from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from timeline.models import Profile

def register(request):
    if request.POST.get('username'):
        try:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            u = User.objects.get(username=request.POST["username"])
            profile = Profile(user=u)
            profile.save()
            return redirect('/account/login')
        except Exception as e:
            return redirect('/register')
    return render(request, 'register/index.html')
