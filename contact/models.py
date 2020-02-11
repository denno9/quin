from django.db import models

# Create your models here.

class Contact(models.Model):
    fullname = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    Subject =models.CharField(max_length=120)
    body = models.CharField(max_length=5000)

    def __str__(self):
        return self.email
