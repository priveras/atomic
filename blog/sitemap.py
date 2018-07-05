from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

class ViewSitemap(Sitemap):

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['blog:index', 'blog:about', 'blog:work', 'blog:hire']

    def location(self, item):
        return reverse(item)
