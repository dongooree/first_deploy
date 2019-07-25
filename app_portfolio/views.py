from django.shortcuts import render
from .models import Portfolio

# Create your views here.

def portfolio(request):
    folfol = Portfolio.objects

    return render(request, 'portfolio.html',
    { 'popo' : folfol } )