# Generated by Django 3.2.9 on 2022-04-07 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20220405_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]