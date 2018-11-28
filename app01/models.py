from django.db import models

# Create your models here.

class Publisher(models.Model):

     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=32)
     city = models.CharField(max_length=32)
     email = models.EmailField()

class Author(models.Model):

     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=32)
     age = models.IntegerField()

class Book(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publish_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publisher = models.ForeignKey("Publisher",on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author")
