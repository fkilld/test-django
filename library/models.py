from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=100)
  def __str__(self):
    return self.name
  
class Category(models.Model):
  cat_name = models.CharField(max_length=100)

  def __str__(self):
    return self.cat_name

class Book(models.Model):
 book_name = models.CharField(max_length=100)
 book_description = models.TextField()
 author = models.ForeignKey(Author, on_delete=models.CASCADE)
 categories = models.ManyToManyField(Category)