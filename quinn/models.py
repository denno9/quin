from django.db import models


class QuinModel(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=2000)
    mission = models.CharField(max_length=500)
    vision  = models.CharField(max_length=500)
    focus = models.CharField(max_length=4000)

