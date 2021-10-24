from django.shortcuts import render
from django.http import request
import requests
from .services import get_infoStats

# Create your views here.
def home(request):
    price,percent_change_24h,percent_change_7d = get_infoStats()
    return render(request, 'stats/home.html',{
        'valor': price,
        'valor24': percent_change_24h,
        'valor7d': percent_change_7d
})