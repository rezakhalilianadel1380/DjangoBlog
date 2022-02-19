from django.db import models
import os
import datetime
from django.db.models import Q
from django.utils.translation import activate
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from jalali_date import date2jalali,datetime2jalali
from nlg_category.models import Category
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe

from nlg_tag.models import Tag
# Create your models here.

def change_name2(instance,filename):
    now=datetime.datetime.now()
    currenttime=now.strftime("%Y__%b__%d__%H__%M__%S")
    name,ext=os.path.splitext(os.path.basename(filename))
    return  f'productgallery/{currenttime}{ext}'


class ArticleManager(models.Manager):
    def search(self,q):
        lookup=(
           Q(title__icontains=q)|
           Q(description__icontains=q)|
           Q(author__icontains=q)|
           Q(tag__name__icontains=q)
        )
        
        return self.get_queryset().filter(lookup,active=True).distinct()




class Article(models.Model):
    title=models.CharField(max_length=120,verbose_name='عنوان')
    description=RichTextUploadingField(verbose_name='توضیحات')
    image=models.ImageField(upload_to=change_name2,blank=True,null=True,verbose_name='عکس')
    active=models.BooleanField(default=False,verbose_name='فعال/غیر فعال ')
    category=models.ManyToManyField(Category,blank=True,verbose_name='دسته بندی ها')
    time=models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=120,blank=True,verbose_name='نویسنده')
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    tag=models.ManyToManyField(Tag,blank=True,verbose_name='برچسب')
    objects=ArticleManager()
    
    class Meta:
        verbose_name='مقاله'
        verbose_name_plural='مقالات'

    def __str__(self):
        return self.title
    
    
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'
    def convert_to_jalali(self):
        month=date2jalali(self.time).strftime('%m')
        monthjalali={
            '01':'فروردین',
            '02':'اردیبهشت',
            '03':'خرداد',
            '04':'تیر',
            '05':'مرداد',
            '06':'شهریور',
            '07':'مهر',
            '08':'آبان',
            '09':'اذر',
            '10':'دی',
            '11':'بهمن',
            '12':'اسفند',         
            } 
        for i in monthjalali:
            if i==month:
                month=monthjalali[i]  
        return date2jalali(self.time).strftime(f'%d{month}')        


class Article_Commnet(models.Model):
    name=models.CharField(max_length=120,verbose_name='نام ')
    email=models.EmailField(max_length=120,verbose_name='ایمیل')
    message=models.TextField(verbose_name='پیام')
    article=models.ForeignKey(Article,on_delete=models.CASCADE,blank=True)
    time=models.DateTimeField(auto_now_add=True)
    allowed=models.BooleanField(default=False,verbose_name='مجاز')
    
    class Meta:
        verbose_name='کامنت'
        verbose_name_plural='کامنت ها'
    def convert_to_jalali(self):
        month=date2jalali(self.time).strftime('%m')
        monthjalali={
            '01':'فروردین',
            '02':'اردیبهشت',
            '03':'خرداد',
            '04':'تیر',
            '05':'مرداد',
            '06':'شهریور',
            '07':'مهر',
            '08':'آبان',
            '09':'اذر',
            '10':'دی',
            '11':'بهمن',
            '12':'اسفند',         
            } 
        for i in monthjalali:
            if i==month:
                month=monthjalali[i]  
        return date2jalali(self.time).strftime(f'%d{month} ,%Y') 
               
    def check_reply(self):
        reply=self.reply_commnet_set.all().filter(allowed=True)
        if reply.exists():
            return  reply
        else:
            return False

    def __str__(self) :
        return self.name
    


class Reply_commnet(models.Model):
    name=models.CharField(max_length=120,verbose_name='نام')
    email=models.EmailField(max_length=120,verbose_name='ایمیل ')
    message=models.TextField(verbose_name='پیام ')
    comment=models.ForeignKey(Article_Commnet,on_delete=models.CASCADE,blank=True,verbose_name='کامنت')
    time=models.DateTimeField(auto_now_add=True)
    allowed=models.BooleanField(default=False,verbose_name='مجاز') 
    class Meta:
        verbose_name='ریپلای کامنت'
        verbose_name_plural=' ریپلای کامنت ها ' 
    def convert_to_jalali(self):
        month=date2jalali(self.time).strftime('%m')
        monthjalali={
            '01':'فروردین',
            '02':'اردیبهشت',
            '03':'خرداد',
            '04':'تیر',
            '05':'مرداد',
            '06':'شهریور',
            '07':'مهر',
            '08':'ابان',
            '09':'اذر',
            '10':'دی',
            '11':'بهمن',
            '12':'اسفند',         
            } 
        for i in monthjalali:
            if i==month:
                month=monthjalali[i]  
        return date2jalali(self.time).strftime(f'%d{month} ,%Y')   

    

    def __str__(self) :
        return self.name
    