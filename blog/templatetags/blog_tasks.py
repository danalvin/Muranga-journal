from ..models import Category, Blog
from django import template
from django.db.models import Count
import requests
from django.shortcuts import render
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

@register.inclusion_tag('sideposts.html')
def show_latest_posts(count = 4, group_name = 'Recent posts'):
    post_list = Blog.objects.order_by('-publishedDate')[:count]
    return{'post_list': post_list, 'group_name': group_name}


@register.inclusion_tag('_categoriessidelist.html')
def show_categories_side():
    categories = Category.objects.annotate(post_count=Count("blog")).filter(post_count__gt=0).order_by('-post_count','title') 
    return{'categories': categories}

@register.inclusion_tag("corona.html")
def corona():
    response = requests.get('http://coronavirus-19-api.herokuapp.com/countries/kenya')
    geodata = response.json()
    return  {
        'Cases': geodata['cases'],
        'todayCases': geodata['todayCases'],
        'deaths': geodata['deaths'],
        'todayDeaths': geodata['todayDeaths'],
        'recovered': geodata['recovered'],
        'active': geodata['active']
    }