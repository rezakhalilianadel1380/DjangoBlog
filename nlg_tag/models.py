from django.db import models
# Create your models here.



class Tag(models.Model):
    name=models.CharField(max_length=100,verbose_name='نام ')
    time=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

    def __str__(self):
        return self.name


