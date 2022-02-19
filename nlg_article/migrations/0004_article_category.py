# Generated by Django 3.2.8 on 2021-10-13 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlg_category', '0001_initial'),
        ('nlg_article', '0003_alter_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, to='nlg_category.Category'),
        ),
    ]
