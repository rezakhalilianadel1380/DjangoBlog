from django.urls import path
from django.urls.conf import include

from it_blog.views import categories
from .views import Article_detail, List_article, List_category, Search, add_comment


urlpatterns = [
    path('articles/',List_article.as_view(),name='articles'),
    path('add-comment',add_comment),
    path('search',Search.as_view()),
    path('categories',categories,name='category'),
    path('article/<pk>',Article_detail.as_view()),
    path('category/<catname>',List_category.as_view()),
    path('hitcount/',include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]

