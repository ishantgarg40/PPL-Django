from django.urls import path
from . import views

app_name = "singlepost"
urlpatterns = [
    path("", views.singlepost, name="singlepost"),
    path("add_comment/", views.add_comment, name="add_comment"),
    path('add_reply/', views.add_reply, name="add_reply")
]