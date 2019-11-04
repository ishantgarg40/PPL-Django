from django.urls import path
from . import views
from ppl import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "timeline"
urlpatterns = [
    path('', views.timeline, name="timeline"),
    path('post/', views.post_upload, name="post_upload"),
    path('change_profile/', views.change_profile, name="change-profile"),
    path('add_categories/', views.add_category, name="add_category"),
]

