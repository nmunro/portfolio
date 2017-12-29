from django.shortcuts import render

from .models import Education


def index(request):
    l = list(Education.objects.all().order_by('-completed'))
    return render(request, 'education/index.html', {"education": l})
