# Generated by Django 3.2.8 on 2021-10-13 15:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nlg_article', '0005_article_commnet'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_commnet',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]