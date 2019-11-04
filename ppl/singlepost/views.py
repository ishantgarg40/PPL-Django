from django.shortcuts import render, redirect, reverse
from timeline.models import Post
from .models import Comment, Reply
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required
def singlepost(request):
    if request.method == "POST":
        post_id = request.POST["post_id"]
    elif request.method == "GET":
        post_id = request.GET["post_id"]
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    comment_reply = dict()
    for comment in comments:
        comment_reply[comment] = Reply.objects.filter(comment=comment)
    if post_id:
        return render(request, 'singlepost/index.html', {'post': post, 'user': request.user, 'comment_reply': comment_reply})
    else:
        return redirect("/timeline")


def add_comment(request):
    post = Post.objects.get(pk=request.POST["post"])
    comment = request.POST["comment"]
    created_on = timezone.now()
    new_comment = Comment(post=post, comment=comment, created_on=created_on)
    new_comment.save()
    return redirect(f"/singlepost?post_id={post.id}")


def add_reply(request):
    comment = Comment.objects.get(pk=request.POST["comment_info"])
    post_id = request.POST["post_id"]
    reply = request.POST["reply"]
    new_reply = Reply(comment=comment, reply=reply)
    new_reply.save()
    return redirect(f"/singlepost?post_id={post_id}")

