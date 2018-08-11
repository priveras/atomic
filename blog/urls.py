from django.conf.urls import url

from . import views

from django.contrib.sitemaps.views import sitemap
from sitemap import ViewSitemap

# a dictionary of sitemaps
sitemaps = {
    'views': ViewSitemap,
}

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^hire/$', views.hire, name='hire'),
    url(r'^services/$', views.ServicesView.as_view(), name='services'),
    url(r'^faq/$', views.FaqView.as_view(), name='faq'),
    url(r'^coming-soon/$', views.SoonView.as_view(), name='soon'),
    url(r'^work/$', views.ProjectListView.as_view(), name='work'),
    url(r'^blog/$', views.BlogListView.as_view(), name='blog'),
    url(r'^thanks/$', views.ThanksView.as_view(), name='thanks'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^blog/(?P<slug>[^\.]+)/$', views.BlogPostView.as_view(), name='blog-post'),
]