from django.shortcuts import render
from django.views import generic
from .models import Freelancer

class DashboardView(generic.TemplateView):
    template_name = "dashboard/index.html"

class StrategyView(generic.TemplateView):
    template_name = "dashboard/ua/strategy.html"

class SeoView(generic.TemplateView):
    template_name = "dashboard/ua/seo.html"

class ObjectiveFirstView(generic.TemplateView):
    template_name = "dashboard/ua/objective-first.html"

class SeoChecklistView(generic.TemplateView):
    template_name = "dashboard/ua/seo-checklist.html"

class FreelancerListView(generic.ListView):
    template_name = 'dashboard/freelancers.html'
    context_object_name = 'freelancers_list'

    def get_queryset(self):
        return Freelancer.objects.order_by('-created_at')
