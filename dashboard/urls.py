from django.conf.urls import url

from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^dashboard/freelancers/$', views.FreelancerListView.as_view(), name='freelancers'),
]