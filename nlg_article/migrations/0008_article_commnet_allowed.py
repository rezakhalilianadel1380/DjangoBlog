# Generated by Django 3.2.8 on 2021-10-20 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlg_article', '0007_reply_commnet'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_commnet',
            name='allowed',
            field=models.BooleanField(default=False),
        ),
    ]
