from django.shortcuts import render, redirect


def index(request):
    return redirect('home/')


def home(request):
    return render(request, 'vizitsite/home.html')


def portfolio(request):
    return render(request, 'vizitsite/portfolio.html')
