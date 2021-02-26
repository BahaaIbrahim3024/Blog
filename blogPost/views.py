from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.db.models import Q
from django.http import JsonResponse
from .models import BlogPost
from account.models import Account
from .forms import CreateBlogPostForm, UpdateBlogPostForm


# Create your views here.
def create_blog_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        post.author = author
        post.save()
        form = CreateBlogPostForm()

    context['create_blog_form'] = form

    return render(request, 'blogPost/create_blog.html', context)


def detail_blog_view(request, slug):
    context = {}
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post
    return render(request, 'blogPost/detail_blog.html', context)


def update_blog_view(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    blog_post = get_object_or_404(BlogPost, slug=slug)
    if blog_post.author != user:
        return HttpResponse("You aren't the owner of this post.")

    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = 'Updated'
            blog_post =obj
    form = UpdateBlogPostForm(
        initial = {
            'title' : blog_post.title,
            'body' : blog_post.body,
            'image' : blog_post.image,
        }
    )
    context['form'] = form
    return render(request, 'blogPost/update_blog.html', context)


# View for delete post
def delete_blog_view(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    blog_post = get_object_or_404(BlogPost, slug=slug)
    if blog_post.author != user:
        return HttpResponse("You aren't the owner of this post.")

    operation = blog_post.delete()
    if operation:
        return redirect("home")
    return render(request, 'home/home.html', context)


# view for set a favorite posts
def favorite_view(request, slug):
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    post = get_object_or_404(BlogPost, slug=slug)
    try:
        if post.isFavorite:
            post.isFavorite = False
        else:
            post.isFavorite = True
        post.save()
    except (KeyError, BlogPost.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return redirect("home")


# define a search function
def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = BlogPost.objects.filter(
            Q(title__icontains=q),
            Q(body__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)
    return list(set(queryset))
