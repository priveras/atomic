from __future__ import unicode_literals

from django.db import models

class Freelancer(models.Model):
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
