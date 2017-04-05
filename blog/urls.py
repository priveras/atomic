from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^hire/$', views.hire, name='hire'),
    url(r'^faq/$', views.FaqView.as_view(), name='faq'),
    url(r'^coming-soon/$', views.SoonView.as_view(), name='soon'),
    url(r'^talent/$', views.TalentView.as_view(), name='talent'),
    url(r'^thanks/$', views.ThanksView.as_view(), name='thanks'),
]