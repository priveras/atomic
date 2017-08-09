from django.shortcuts import render
from django.views import generic
from .models import Freelancer

class DashboardView(generic.TemplateView):
    template_name = "dashboard/index.html"

class FreelancerListView(generic.ListView):
    template_name = 'dashboard/freelancers.html'
    context_object_name = 'freelancers_list'

    def get_queryset(self):
        return Freelancer.objects.order_by('-created_at')
