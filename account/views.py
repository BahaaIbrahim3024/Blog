from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, LoginForm, UpdateAccount
from blogPost.models import BlogPost


# Create your views here.
def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data['email'].lower()
            raw_password = form.cleaned_data['password1']
            user.set_password(raw_password)
            user.save()
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    context = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print("login")
                return redirect('home')

    else:
        form = LoginForm()
    context['login_form'] = form
    return render(request, "account/login.html", context)


def login_view2(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                print('login')
                return redirect('home')
    else:
        form = LoginForm()
    context['login_form'] = form
    return render(request, 'account/login.html', context)


def edit_account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {}
    if request.POST:
        form = UpdateAccount(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                'email': request.POST['email'],
                'username': request.POST['username'],
                'first_name': request.POST['first_name'],
                'last_name': request.POST['last_name'],
                'age': request.POST['age'],
                'gender': request.POST['gender'],
            }
            form.save()
            context['success_message'] = 'Updated'
    else:
        form = UpdateAccount(
            initial={
                'email': request.user.email,
                'username': request.user.username,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'age': request.user.age,
                'gender': request.user.gender,

            }
        )
    context['account_form'] = form

    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts
    return render(request, 'account/account.html', context)


def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html',{})
