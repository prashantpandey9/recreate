from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Contactus(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,blank=False)
    text = models.TextField(max_length=2500, blank=False)

# class Post(models.Model):
#     posted_by = models.CharField(max_length=50)
#     posted_on = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=False)
#     cover = models.ImageField(verbose_name='Cover', blank=True)
#     content = models.TextField(max_length=1000)
#     likes = models.ManyToManyField(User, related_name='postlikes', blank=True)
#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ['-posted_on']

#     @property
#     def postcomment(self):
#         return self.postcomment_set.all().order_by('-date')

#     def FORMAT(self):
#         from django.utils.timesince import timesince
#         if timesince(self.posted_on) == '0 minutes':
#             return "just now"
#         return timesince(self.posted_on) + " ago"

# class PostComment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#     commented_by = models.CharField(max_length=50)
#     content = models.TextField(max_length=500, blank=True)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.commented_by}'s comment on {self.post.posted_by}'s post"
    
#     class Meta:
#         ordering=['-date']
    
