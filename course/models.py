from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) | 
                         Q(description__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups          
        return qs

class LessionManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) | 
                         Q(description__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups          
        return qs

class ProfileManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) | 
                            Q(description__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups          
        return qs
      

class Lession(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    # slug = models.SlugField(blank=True, unique=True)
    feature = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    less_objects = LessionManager()    

    def __str__(self):
        return self.title

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    # slug = models.SlugField(blank=True, unique=True)
    publish_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    post_objects = PostManager() # The Dahl-specific manager.


    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    # slug = models.SlugField(blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    prof_objects = ProfileManager()

    def __str__(self):
        return self.title

