# about/views.py
from django.views.generic import TemplateView, ListView
from .models import CompanyInfo, TeamMember, Department

class AboutPageView(TemplateView):
    template_name = 'about/about.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['company'] = CompanyInfo.objects.first()
    #     # context['values'] = CompanyValue.objects.all()
    #     # context['certifications'] = CompanyCertification.objects.all()
    #     context['featured_team'] = TeamMember.objects.filter(is_featured=True, is_active=True)
    #     return context


class TeamPageView(ListView):
    template_name = 'about/team.html'
    # context_object_name = 'departments'
    # model = Department
    
    # def get_queryset(self):
    #     # This will prefetch the related team members to prevent additional database queries
    #     return Department.objects.prefetch_related('members')