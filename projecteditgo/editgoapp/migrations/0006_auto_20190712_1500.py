# Generated by Django 2.1.8 on 2019-07-12 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editgoapp', '0005_auto_20190709_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='creator',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]