from django.db import models

class IlmiyBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name
