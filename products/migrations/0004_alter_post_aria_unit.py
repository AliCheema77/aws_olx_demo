# Generated by Django 3.2.9 on 2022-04-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_post_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='aria_unit',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]