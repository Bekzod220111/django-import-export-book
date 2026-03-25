from django.db import models

# Create your models here.

class Author(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ism} {self.familya}"


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title