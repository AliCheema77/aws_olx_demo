# Generated by Django 3.2.9 on 2022-05-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_post_viewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
