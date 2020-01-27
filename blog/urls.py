from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('', Bloglist.as_view(), name="blog"),
    path('/<int:id>', BlogDetailView.as_view(), name="blog-details"),
]