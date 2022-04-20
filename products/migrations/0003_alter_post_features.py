# Generated by Django 3.2.9 on 2022-04-01 04:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_post_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='features',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=250, null=True), blank=True, null=True, size=50),
        ),
    ]