from django.db import models
import uuid

class Book(models.Model):
    id = models.CharField(max_length=10, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    createddate = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)
    
    def __str__(self) -> str:
        return self.title

class Author(models.Model):
    books = models.ManyToManyField(Book, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=10, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __unicode__(self):
        return u'%s %s' % (self.name)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    createddate = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=10, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.name

# Create your models here.


