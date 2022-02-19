from itertools import product
from django import forms
from django.contrib.auth.models import User
from django.core import validators


class Commnet_Form(forms.Form):
    name = forms.CharField( 
    widget=forms.TextInput(attrs={'placeholder': 'نام شما',' id':"exampleInput"})
    )
    article_id = forms.IntegerField(widget=forms.HiddenInput(attrs={}),
    
    )
    reply_id = forms.IntegerField(widget=forms.HiddenInput(attrs={'id':'reply_comment'}),
    
    )

    email = forms.EmailField(label='ایمیل',  widget=forms.EmailInput(
        attrs={
            'placeholder':"ایمیل شما (الزامی)",
            'id':'exampleInputEmail1',
            'aria-describedby':'emailHelp',

            }),
         )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'عنوان','class':"w-100" ,'rows':"5"}),
        
    )