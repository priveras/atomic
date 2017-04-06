from __future__ import unicode_literals

from django.db import models
import datetime

class Post(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	project_choices = (
    	('mobile', 'Mobile'),
    	('web', 'Web'),
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

class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile_image = models.FileField(upload_to='images/%Y%m%d')
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    overview = models.TextField()
    skills = models.TextField()
    english_choices = (
        ('poor', 'Poor'),
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        )
    english = models.CharField(choices=english_choices, max_length=200)
    work_history = models.TextField()

    def __str__(self):
        return self.email