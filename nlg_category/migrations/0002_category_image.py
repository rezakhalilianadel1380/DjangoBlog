# Generated by Django 3.2.8 on 2021-10-14 12:32

from django.db import migrations, models
import nlg_category.models


class Migration(migrations.Migration):

    dependencies = [
        ('nlg_category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=nlg_category.models.change_name2),
        ),
    ]
