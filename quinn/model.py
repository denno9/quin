from django.db import models



class TheTeam(models.Model):
    firstname = models.CharField(max_length=120)
    middlename = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone =models.CharField(max_length=120)
    description = models.CharField(max_length=5000)
    image = models.ImageField()



    def __str__(self):
        return self.firstname