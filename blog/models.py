from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
import datetime

class Post(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	project_choices = (
        ('web', 'Web Development'),
    	('mobile', 'Mobile Development'),
        ('strategy', 'Digital Strategy'),
    	('other', 'Other'),
    	)
	project = models.CharField(choices=project_choices, max_length=200)
	status_choices = (
    	('new', 'New'),
    	('existing', 'Existing'),
    	)
	status = models.CharField(choices=status_choices, max_length=200)
	timeline_choices = (
    	('now', 'Now'),
    	('week', 'One Week'),
    	('month', 'One Month'),
    	('months', 'Two Months'),
    	)
	timeline = models.CharField(choices=timeline_choices, max_length=200)
	created_at = models.DateTimeField(db_index=True, auto_now_add=True, null=True)

	def __str__(self):
		return self.email

class Blog(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.FileField(upload_to='images/%Y%m%d', blank=True)
    is_draft = models.BooleanField(default=False, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog-post', kwargs={'slug':self.slug})
