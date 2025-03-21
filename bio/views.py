from django.shortcuts import render
from django.views.generic import ListView
# from .models import CompanyInfo, TeamMember, Department


app_name = 'bio'

# Create your views here.
def aboutUs(request):
    # about = About.objects.all()
    # context = {
    #     "about" : about,
    # }

    return render(request, 'bio/bio.html',)