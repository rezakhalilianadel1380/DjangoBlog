from django.contrib import messages
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import html
from hitcount.views import HitCountDetailView
from nlg_article.forms import Commnet_Form
from .models import Article, Article_Commnet, Reply_commnet
from django.views.generic import ListView
from nlg_category.models import Category
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags




#list_article 
class List_article(ListView):
    """ retrun list of articles """
    model=Article
    template_name='list_view.html'
    queryset=Article.objects.filter(active=True).all().order_by('-time')
    paginate_by=9
    def get_context_data(self, *args ,object_list=None,**kwargs):
        context=super(List_article,self).get_context_data(*args,**kwargs)
        return context







class Search(ListView):
    template_name='search_tem.html'
    paginate_by=10
    def get_context_data(self, *args ,**kwargs):
        context=super(Search,self).get_context_data(*args,**kwargs)
        return context
    
    def get_queryset(self):
        request=self.request
        search=request.GET.get('q')   
        if search=='':
            return Article.objects.filter(active=True)[0:6]
        articles:Article=Article.objects.search(search)
        if not articles.exists():
            messages.warning(request,'مقاله ای یافت نشد ')
            return Article.objects.filter(active=True).order_by('?')[0:6]
        return articles



class List_category(ListView):
    template_name='category_list.html'
    paginate_by=10
    def get_context_data(self, *args ,object_list=None,**kwargs):
        context=super(List_category,self).get_context_data(*args,**kwargs)
        context['categoryname']=Category.objects.get(name=self.kwargs.get('catname'))
        return context
    
    def get_queryset(self):
        name=self.kwargs['catname']
        article=Article.objects.filter(category__name=name)
        if not article.exists():
            messages.warning(self.request,'هیچ مقاله ای  یافت نشد ')
        return article




class Article_detail(HitCountDetailView):
    model=Article
    template_name = "detail_view.html"
    paginate_by=5
    count_hit = True
    context_object_name = 'article'
    
    def get_context_data(self,*args, **kwargs):
        context = super(Article_detail, self).get_context_data(**kwargs)
        request=self.request
        article_id=self.kwargs.get('pk')
        comment_form=Commnet_Form(request.POST or None,initial={'article_id':article_id,'reply_id':800})
        article=Article.objects.get(id=article_id)
        categories=Category.objects.filter(active=True).all()
        last_article=Article.objects.order_by('-time')[0:5]
        comments=Article_Commnet.objects.filter(article=article,allowed=True).order_by('-time')
        context.update({
        'article':article,
        'categories':categories,
        'last_articles':last_article,
        'comment_form':comment_form,
        'comments':comments,     
            })
        return context

    def get_object(self):
        article_id=self.kwargs.get('pk')
        article=get_object_or_404(Article,id=article_id)
        if article is None or not article.active:
            raise Http404
        return article
    
def send_email(subject,to,template_name,context):
    html_message=render_to_string(template_name,context)
    plain_message=strip_tags(html_message)
    send_mail(subject,plain_message,'narangblogpaya@gmail.com',to,html_message=html_message)

#add commnet post from detailview   
def add_comment(request):
    comment_form=Commnet_Form(request.POST or None)

    if comment_form.is_valid():
        email=comment_form.cleaned_data.get('email')
        name=comment_form.cleaned_data.get('name')
        message=comment_form.cleaned_data.get('message')
        article_id=comment_form.cleaned_data.get('article_id')
        reply_id=comment_form.cleaned_data.get('reply_id')
        if reply_id!=800:
            comment=Article_Commnet.objects.get(id=reply_id)
            Reply_commnet.objects.create(name=name,email=email,message=message,comment=comment)
            messages.success(request,'کامنت شما اضافه شد ')
            return redirect(f'article/{article_id}')         
        article=Article.objects.get(id=article_id)
        Article_Commnet.objects.create(email=email,name=name,message=message,article=article)
        send_email('نارنج بلاگ ',[email],'email.html',{'title':f'{name}','description':'کامنت شما باموفقیت اضافه شد  '})
        messages.success(request,'کامنت شما اضافه شد ')
        return redirect(f'article/{article_id}')
    messages.error(request,'کامنت ثبت نشد تمامی  فیلد هارا کامل فرمایید')
    return redirect(f'article/{comment_form.cleaned_data.get("article_id")}')         
 


# def detail_view(request,articleid):
#     comment_form=Commnet_Form(request.POST or None,initial={'article_id':articleid})
#     article=Article.objects.get(id=articleid)
#     categories=Category.objects.filter(active=True).all()
#     last_article=Article.objects.order_by('-time')[0:5]
#     comments=Article_Commnet.objects.filter(article=article)
#     context={
#         'article':article,
#         'categories':categories,
#         'last_articles':last_article,
#         'comment_form':comment_form,
#         'comments':comments,
      
#     }
#     return render(request,'detail_view.html',context)
