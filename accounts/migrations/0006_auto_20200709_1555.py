# Generated by Django 3.0.7 on 2020-07-09 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200709_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='withdrawal',
            old_name='sponsored_post_checked',
            new_name='withdrawn',
        ),
    ]
