from django.conf.urls import url

from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^dashboard/user_acquisition/strategy$', views.StrategyView.as_view(), name='strategy'),
    url(r'^dashboard/user_acquisition/seo$', views.SeoView.as_view(), name='seo'),
    url(r'^dashboard/user_acquisition/seo/checklist$', views.SeoChecklistView.as_view(), name='seo-checklist'),
    url(r'^dashboard/user_acquisition/objective-first$', views.ObjectiveFirstView.as_view(), name='objective-first'),
    url(r'^dashboard/freelancers/$', views.FreelancerListView.as_view(), name='freelancers'),
]