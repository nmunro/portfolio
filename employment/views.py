from django.shortcuts import render
from .models import Employer

def index(request):
    def tmp(em):
        if em.ended == None:
            em.ended = "Present"
        return em

    l = list(map(tmp, Employer.objects.all().order_by('-started')))
    return render(request, 'employment/index.html', {"employers": l})
