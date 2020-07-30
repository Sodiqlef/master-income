# Generated by Django 3.0.7 on 2020-07-23 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_regularcoupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regularcoupon',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='regular', to=settings.AUTH_USER_MODEL),
        ),
    ]
