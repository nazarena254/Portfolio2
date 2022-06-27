from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

class PersonalInformation(models.Model):
    name_complete = models.CharField(max_length=50, blank=True, null=True)
    mini_about = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    resume = models.FileField(upload_to='resume', blank=True, null=True)
    # Social Network
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    resumeurl = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name_complete


class About(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description1 = models.TextField(blank=False, null=True)

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    technologies = models.TextField(max_length=230, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    project_pic = CloudinaryField('image')

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    msg = models.TextField(max_length=100, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    email = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title



