# Generated by Django 3.0.7 on 2020-07-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterincome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsoredpost',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='sponsoredpost',
            name='feature_image',
            field=models.ImageField(blank=True, null=True, upload_to='sponsored_image'),
        ),
        migrations.AlterField(
            model_name='sponsoredpost',
            name='subject',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sponsoredpost',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]