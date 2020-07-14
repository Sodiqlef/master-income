# Generated by Django 3.0.7 on 2020-07-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawal',
            name='activities_earning',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='guider_bonus',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='sponsored_post_checked',
            field=models.BooleanField(default=False),
        ),
    ]
