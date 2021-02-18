from django.shortcuts import render
from blogPost.models import BlogPost
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blogPost.views import get_blog_queryset


# set number of posts per page (in develop env = 1 & in production = 10)
BLOG_POST_PER_PAGE = 1


# Create your views here.
def home_screen_view(request):
    context = {}
    # add query to home screen for search
    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = query
    # Sort all of blog posts by updated date
    posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
    context['posts'] = posts

    # Pagination
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(posts, BLOG_POST_PER_PAGE)
    try:
        posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        posts = blog_posts_paginator.page(BLOG_POST_PER_PAGE)
    except EmptyPage:
        posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)
    context['posts'] = posts

    return render(request, 'home/home.html', context)
