from django.shortcuts import redirect, render
from django.http.response import Http404
from nlg_article.models import Article
from nlg_category.models import Category
from nlg_slider.models import Slider
from django.apps import apps
from nlg_article.models import Article_Commnet
def homepage(request):
    articles=Article.objects.order_by('-time')[0:6]
    most_visited=Article.objects.order_by('-hit_count_generic__hits')[0:8]
    category=Category.objects.filter(favorite=True)[0:4]
    category2=Category.objects.filter(favorite=True)[4:6]
    slider=Slider.objects.all()
    tst=Article.objects.get(id=9)
    context={
        "articles":articles,
        'visit':most_visited,
        'cat1':category,
        'cat2':category2,
        'sliders':slider,
        'tst':tst
        
    }
    return render(request,'homepage.html',context)


def contact_us(request):
 
    context={
      
    }
    return render(request,'contact_us.html',context)


def categories(request):
    category=Category.objects.all()
    context={
      'cat1':category,
    }
    return render(request,'category.html',context)

def custom(request):
    ARTICLE_number=len(Article.objects.all())
    context={
      "article_num":ARTICLE_number,
    }
    return render(request,'starter.html',context)