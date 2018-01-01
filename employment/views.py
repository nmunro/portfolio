from django.shortcuts import render
from .models import Employer

def index(request):
    l = list(Employer.objects.all().order_by('-started'))
    return render(request, 'employment/index.html', {'employers': l, 'active': 'employment'})
