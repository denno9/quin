from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe
from django.db.models.signals import pre_save
import random
import os
# Create your models here.

def get_filename_ext(filepath):
    base_name= os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext
def upload_image_path(instance,filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "members/{final_filename}".format(final_filename=final_filename )

# class TeamImage(models.Model):
#     image = models.ImageField(upload_to=upload_image_path,blank=True,null=True)
#     filename =models.CharField(max_length=255, default="quinImage")
    
#     def __str__(self):
#         return self.filename

class TheTeam(models.Model):
    image = models.ImageField(upload_to=upload_image_path,blank=True,null=True)
    fullname = models.CharField(max_length=520,blank=True)
    firstname = models.CharField(max_length=120)
    middlename = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True ,max_length=5000)
    active = models.BooleanField(default=False)
    nt = models.BooleanField(default=False)

    def image_tag(self):
        return mark_safe('<img src="/members/%s" width="150" height="150" />' %(self.image))

    image_tag.short_description = "Image Preview"
   



    def __str__(self):
        return self.firstname


def fullname_pre_save_receiver(sender,instance,*args,**kwargs):
    fullname =  "{} {} {}".format(instance.firstname, instance.middlename, instance.lastname)
    if not instance.fullname or instance.fullname != fullname.title():
         instance.fullname = fullname.title()
        

pre_save.connect(fullname_pre_save_receiver, sender=TheTeam)

