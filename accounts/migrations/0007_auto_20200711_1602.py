# Generated by Django 3.0.7 on 2020-07-11 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200709_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='withdrawal',
            old_name='withdrawn',
            new_name='sponsored_post_check',
        ),
        migrations.RemoveField(
            model_name='withdrawal',
            name='account_details',
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='account_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='account_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='bank_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
