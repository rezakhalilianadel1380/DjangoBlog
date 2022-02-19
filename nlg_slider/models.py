from django.db import models
from django.db.models.base import Model

# Create your models here.
import os,datetime
def change_name2(instance,filename):
    now=datetime.datetime.now()
    currenttime=now.strftime("%Y__%b__%d__%H__%M__%S")
    name,ext=os.path.splitext(os.path.basename(filename))
    return  f'slider/{currenttime}{ext}'


class Slider(models.Model):
    title=models.CharField(max_length=50,verbose_name='عنوان عکس')
    image=models.ImageField(upload_to=change_name2,blank=True,null=True,verbose_name='عکس')
    
    class Meta:
        verbose_name='اسلاید'
        verbose_name_plural='اسلایدر '
    def __str__(self):
        return self.title