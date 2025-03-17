from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
app_name = 'core'

class HomeView(TemplateView):
    template_name = 'core/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['services'] = Service.objects.all()[:3] # Display only 3 services on the home page
    #     # context['recent_posts'] = Post.objects.filter(status='published').order_by('-created_on')[:3]  # Display only 3 services on the home page
    #     return context