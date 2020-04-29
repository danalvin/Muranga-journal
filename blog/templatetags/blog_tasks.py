from ..models import Category, Blog
from django import template
from django.db.models import Count

register = template.Library()


@register.simple_tag
def total_posts():
    """ Returns total posts """
    return Post.published.count()

@register.inclusion_tag('blog/_search_box.html')
def search_box():
    form = SearchForm()
    return{'form': form}

@register.inclusion_tag('_categorieslist.html')
def show_categories():
    categories = Category.objects.annotate(post_count=Count("blog")).filter(post_count__gt=0).order_by('-post_count','title') 
    #categories = Category.objects.annotate(post_count=Count("blog_posts")).filter(post_count__gt=0).order_by('name')
    # categories = Category.objects.all().order_by('name')
    return{'categories': categories}

@register.inclusion_tag('blog/_sideposts.html')
def show_latest_posts(count = 5, group_name = 'Recent posts'):
    post_list = Blog.published.order_by('-published_date')[:count]
    return{'post_list': post_list, 'group_name': group_name}
