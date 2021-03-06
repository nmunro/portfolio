from django.shortcuts import render
from .models import Proverb

def index(request):
    proverbs = list(Proverb.objects.all().order_by("order"))
    return render(request, 'proverbs/index.html', {'proverbs': proverbs, 'active': 'proverbs'})
