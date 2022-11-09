from django.shortcuts import render

from .models import (Home, Category, About, Portfolio, Profile, Skills) 

def index(request):

    # home
    home = Home.objects.latest('datetime_modified')

    # about
    about = About.objects.latest('datetime_modified')
    profiles = Profile.objects.filter(about=about)

    # skills
    categories = Category.objects.all()

    # portfolios
    portfolios = Portfolio.objects.all()
    
    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
    }

    return render(request, 'mahdi/index.html', context)
