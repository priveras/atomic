from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from .models import Blog

class ViewSitemap(Sitemap):

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['blog:index', 'blog:about', 'blog:work', 'blog:hire', 'blog:blog']

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Blog.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.created_at