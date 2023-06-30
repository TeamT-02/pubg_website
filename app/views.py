from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.EmailBackEnd import EmailBackEnd
from app.models import *


def index(request):
    brand_img = Home.objects.order_by('-id')[:3]
    know_about = Know_about_us.objects.order_by('-id')[:1]
    images = Images.objects.order_by('-id')[:7]
    team = Website_team.objects.order_by('-id')[:4]
    home_video = Home_Video.objects.order_by('-id')[:1]
    home_seasons = Home_seasons.objects.order_by('-id')[:3]
    home_seasons_step = Home_seasons_step.objects.filter()
    ctx = {
        'brand_img': brand_img,
        'know_about': know_about,
        'images': images,
        'team': team,
        'home_video': home_video,
        'home_seasons': home_seasons,
        'home_seasons_step': home_seasons_step,
    }
    return render(request, 'index.html', ctx)


def about(request):
    about_know = Big_about.objects.order_by('-id')[:1]
    team = Website_team.objects.order_by('-id')[:4]
    ctx = {
        'about_know': about_know,
        'team': team
    }
    return render(request, 'about-us.html', ctx)


def tournament(request):
    lucks = Tournament_Lucky.objects.order_by('-id')[:1]
    ctx = {
        'lucks': lucks
    }
    return render(request, 'tournament.html', ctx)


def tournament_detail(request):
    return render(request, 'tournament-details.html')


def LOGIN(request):
    return render(request, 'registration/login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'),
                                         password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('super_admin')
            elif user_type == '2':
                return redirect('index')
            elif user_type == '3':
                return redirect('index')
            else:
                messages.error(request, 'Email and  Password Are Invalid !')
                return redirect('login')
        else:
            messages.error(request, 'Email and  Password Are Invalid !')
            return redirect('login')
    return None


def doLogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        'user': user
    }
    return render(request, 'registration/profile.html', context)


@login_required(login_url='login')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # username = request.POST.get('username')
        password = request.POST.get('password')
        about = request.POST.get('about')
        print(profile_pic)
        try:
            customuser = CustomUser.objects.get(id=request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.about = about

            if password != None and password != "":
                customuser.set_password(password)
            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, 'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.error(request, 'Failed To Update Your Profile')

    return render(request, 'registration/profile.html')
