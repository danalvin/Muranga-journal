from django.shortcuts import render
from .models import Blog
from django.utils import timezone

from django.views.generic import ListView, DetailView
from django.http import Http404, HttpResponseRedirect

# Create your views here.


class Bloglist(ListView):
    template_name = "blog.html"
    model = Blog
    paginate_by = 3
    context_object_name = 'post'


    def get_queryset(self):
        return self.model.objects.all()[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["HOT"] = self.model.objects.filter(published_date__month=timezone.now().month)[:3]
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog-details.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'


    def get_object(self, queryset=None):
        obj = super(BlogDetailView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Blog does not exist")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("Blog does not exist")
        context = self.get_context_data(object= self.object)
        return self.render_to_response(context)
