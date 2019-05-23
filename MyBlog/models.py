from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Category(models.Model):
    catName = models.CharField(max_length=20, null=False)
    catKey = models.CharField(max_length=16, null=False)
    catDescription = models.CharField(max_length=1000, null=True)
    catViews = models.IntegerField(default=0)
    def __str__(self):
        return self.catName

class Article(models.Model):
    artName = models.CharField(max_length=200, null=False)
    artContent = models.TextField()
    artAuthor = models.CharField(max_length=100, null=False)
    artDateCreate = models.DateTimeField(auto_now=True)
    artDesImg = models.CharField(max_length=255, null=False)
    artCatID = models.ForeignKey(Category,verbose_name='catName', on_delete=models.PROTECT)
    artView = models.IntegerField(default=0)
