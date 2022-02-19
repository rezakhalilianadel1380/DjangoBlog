from django.db import models
import os,datetime
# Create your models here.

def change_name2(instance,filename):
    now=datetime.datetime.now()
    currenttime=now.strftime("%Y__%b__%d__%H__%M__%S")
    name,ext=os.path.splitext(os.path.basename(filename))
    return  f'category/{currenttime}{ext}'


class Category(models.Model):
    title=models.CharField(max_length=120,verbose_name='عنوان')
    name=models.CharField(max_length=120,verbose_name='نام')
    active=models.BooleanField(default=False,verbose_name='فعال/غیر فعال ')
    image=models.ImageField(null=True,blank=True,upload_to=change_name2,verbose_name='عکس')
    time=models.DateTimeField(auto_now_add=True)
    favorite=models.BooleanField(default=False,verbose_name='مورد علاقه')
    class Meta:
        verbose_name='دسته بندی '
        verbose_name_plural=' دسته بندی ها'

    def __str__(self):
        return self.title