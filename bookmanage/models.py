from django.db import models
#此处添加
# Create your models here.

class Author(models.Model):
    AuthorID = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    Country = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    ISBN = models.IntegerField(unique=True)
    Title = models.CharField(max_length=100)
    AuthorID = models.IntegerField()
    Publisher = models.CharField(max_length=100)
    PublicationDate = models.DateField(blank= True,null=True)
    price = models.FloatField()

    def __unicode__(self):
        return self.Title
