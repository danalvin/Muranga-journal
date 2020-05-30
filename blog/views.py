from django.shortcuts import render
from .models import Blog
from django.utils import timezone
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from django.views.generic import ListView, DetailView
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.apps import apps

# Create your views here.


#=================================================================


class Bloglist(ListView):
    template_name = "blog.html"
    model = Blog
    paginate_by = 8  
    context_object_name = 'post'


    def get_queryset(self):
        return self.model.objects.all().order_by('-publishedDate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trendings"] = self.model.objects.filter(publishedDate__month=timezone.now().month)[:3]
        return context

#=================================================================


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog-details.html"
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



#=================================================================

class PostList1(ListView):
    template_name = 'post_list.html'
    model = Blog
    paginate_by = 8
    context_object_name = 'posts'

    def get_queryset(self, **kwargs):
        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        posts=Blog.objects.filter(category=self.category.id)
        return Blog.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(PostList1, self).get_context_data(**kwargs)
        context['category'] = self.category
        print(context)
        return context



#======================================================================

def error_404(request, exception):
       
        return render(request,'404.html', data)

#=================================================================


def error_500(request):
        data = {}
        return render(request,'500.html', data)
        
#=================================================================



def error_403(request):
        data = {}
        return render(request,'404.html', data)

#=================================================================
