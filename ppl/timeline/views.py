from datetime import datetime
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import FileSystemStorage
from PIL import Image
from django.shortcuts import render, redirect
from .models import *
import sys


@login_required
def timeline(request):
    if request.user:
        user_posts = Post.objects.all().order_by('created_at')[::-1]
        categories = Categories.objects.all()
        user = User.objects.get(username=request.user)
        if hasattr(user, 'profile'):
            return render(request, 'timeline/index.html', {'categories': categories, 'user': request.user, 'user_posts': user_posts,
                                                           'user_profile': user.profile})
        else:
            return render(request, 'timeline/index.html', {'categories': categories, 'user': request.user, 'user_posts': user_posts})


def post_upload(request):
    if request.method == 'POST' and request.FILES['image_post']:
        myfile = request.FILES['image_post']
        myfile = compress_image(myfile)
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
        post = Post(image=myfile, created_by=request.user, image_url=myfile, created_at=datetime.now())
        post.save_post(request)
        return redirect('/timeline')
    return render(request, 'timeline/index.html')


def compress_image(uploaded_image):
    image_temporary = Image.open(uploaded_image)
    outputIoStream = BytesIO()
    image_temporary_resized = image_temporary.resize((500, 500))
    image_temporary_resized.save(outputIoStream, format='PNG', quality=60)
    outputIoStream.seek(0)
    uploaded_image = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % uploaded_image.name.split('.')[0], 'image/jpeg',
                                         sys.getsizeof(outputIoStream), None)
    return uploaded_image


def change_profile(request):
    profile_pic = request.FILES["profile_pic"]
    description = request.POST["description"]
    user = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user)
    user_profile.image = profile_pic
    user_profile.description = description
    user_profile.save()
    return redirect('/timeline')


def add_category(request):
    image = request.FILES["category"]
    name = request.POST["name"]
    category = Categories(image=image, name=name)
    category.save()
    return redirect("/timeline")



