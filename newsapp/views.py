# newsapp/views.py

from django.shortcuts import render

def home_view(request):
    return render(request, 'newsapp/home.html')

def sports_view(request):
    news_list = [
        'India wins the cricket series!',
        'Ronaldo scores a hat trick.',
        'Olympics 2026 preparations begin.',
    ]
    context = {
        'category': 'Sports',
        'news_list': news_list,
    }
    return render(request, 'newsapp/news.html', context)

def business_view(request):
    news_list = [
        'Sensex hits all time high.',
        'RBI holds interest rates steady.',
        'Tata launches new EV model.',
    ]
    context = {
        'category': 'Business',
        'news_list': news_list,
    }
    return render(request, 'newsapp/news.html', context)

def entertainment_view(request):
    news_list = [
        'Bollywood blockbuster breaks records.',
        'New music album drops this Friday.',
        'Award season nominations announced.',
    ]
    context = {
        'category': 'Entertainment',
        'news_list': news_list,
    }
    return render(request, 'newsapp/news.html', context)

