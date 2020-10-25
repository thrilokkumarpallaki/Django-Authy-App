from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

# Import Custom Logic Here
from .utils import convert_str_to_date

# Import Models Here
from .models import Profile


# Create your views here.
def index(request):
    return render(request, 'auth/index.html')


@require_http_methods(['GET', 'POST'])
def user_login(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        # authenticate & login user
        lgn_user = authenticate(request, username=username, password=password)
        if lgn_user is not None:
            login(request, lgn_user)
            return redirect(reverse('authy:home', kwargs={'user': lgn_user}))
        else:
            return render(request, 'auth/login.html', {'lgn_error': 'Invalid Credentials.'})


def user_logout(request):
    if request.user.is_authenticated:
        # logout user
        logout(request)
        return redirect(reverse('authy:index'))
    else:
        return render(request, 'auth/index.html')


@require_http_methods(['GET', 'POST'])
def user_signup(request):
    if request.method == 'GET':
        return render(request, 'auth/signup.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        dob = request.POST['dob']
        gender = request.POST['gender']

        # convert dob string to date type
        user_dob = convert_str_to_date(dob)

        # create user
        user = User.objects.create_user(username=username, email=email, password=password)

        # save profile
        Profile.objects.create(user=user, first_name=first_name, last_name=last_name, dob=user_dob, gender=gender)

        return redirect(reverse('authy:login'))


@login_required(login_url='/auth/login')
def home(request, user):
    user = get_object_or_404(User, username=user)
    return render(request, 'auth/home.html', {'user': user})


@login_required(login_url='/auth/login')
def profile_settings(request, user):
    if request.user.is_authenticated:
        user = request.user.username
        user_obj = get_object_or_404(User, username=user)
        return render(request, 'auth/user_profile_settings.html', {'user': user_obj})
    else:
        return redirect(reverse('authy:login'))
