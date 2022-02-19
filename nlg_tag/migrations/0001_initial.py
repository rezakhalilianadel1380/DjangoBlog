# Generated by Django 3.2.8 on 2021-10-31 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nlg_article', '0011_reply_commnet_allowed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام ')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('articles', models.ManyToManyField(blank=True, to='nlg_article.Article', verbose_name='مقاله')),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ ها',
            },
        ),
    ]