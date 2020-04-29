from django.urls import path
from .views import *
from . import views

app_name = "blog"

urlpatterns = [
    path('', Bloglist.as_view(), name="blog"),
    path('article/<slug:slug>', BlogDetailView.as_view(), name="blog-details"),
    path('category/<slug:category_slug>/', views.PostList, name = 'post_list_by_category'),
]
handler404 = 'blog.views.error_404'
handler500 = 'blog.views.error_500'
handler500 = 'blog.views.error_403'