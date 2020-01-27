from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('blog', Bloglist.as_view(), name="blog"),
    path('blog/<int:id>', BlogDetailView.as_view(), name="blog-details"),
]