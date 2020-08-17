from django.db import models
from django.urls import reverse
from quinn.utils import unique_id_generator
from quinn.utils import unique_slug_generator
from django.db.models.signals import pre_save
import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=120)
    body = RichTextField(blank=True,null=True ,max_length=5000)
    slug = models.SlugField(blank=True,unique=True)
    date = models.DateTimeField(auto_now_add=True)
    date_added = models.DateTimeField()
    published = models.BooleanField(default=False)


    def  get_absolute_url(self):
        return reverse('blog', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title


def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=BlogPost)