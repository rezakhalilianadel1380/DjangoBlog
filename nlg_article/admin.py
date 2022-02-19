from django.contrib import admin

from .models import Article, Article_Commnet, Reply_commnet

# Register your models here.

class Admin_Comment(admin.ModelAdmin):
    list_display=['__str__','allowed','message','time']
    list_filter=['allowed']
    list_editable=['allowed']
    class Meta:
        model=Article_Commnet

class Admin_Aritcle(admin.ModelAdmin):
    list_display=['image_tag','__str__','active']
    search_fields=['id','title','description']
    list_filter=['active']
    list_editable=['active']
    class Meta:
        model=Article

class Admin_replycomment(admin.ModelAdmin):
    list_display=['__str__','allowed']
    list_filter=['allowed']
    list_editable=['allowed']
    class Meta:
        model=Reply_commnet


admin.site.register(Article,Admin_Aritcle)
admin.site.register(Article_Commnet,Admin_Comment)
admin.site.register(Reply_commnet,Admin_replycomment)
