# about/views.py
from django.shortcuts import render
from django.views.generic import ListView
# from .models import CompanyInfo, TeamMember, Department


app_name = 'about'

# Create your views here.
def aboutUs(request):
    # about = About.objects.all()
    # context = {
    #     "about" : about,
    # }

    return render(request, 'about/bio.html',)


# class TeamPageView(ListView):
#     template_name = 'about/team.html'
#     context_object_name = 'departments'
#     model = Department
    
#     def get_queryset(self):
#         # This will prefetch the related team members to prevent additional database queries
#         return Department.objects.prefetch_related('members')