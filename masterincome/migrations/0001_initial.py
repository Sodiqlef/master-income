# Generated by Django 3.0.7 on 2020-06-23 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SponsoredPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subject', models.TextField()),
                ('feature_image', models.ImageField(upload_to='sponsored_image')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('post', models.TextField()),
                ('post_image', models.ImageField(null=True, upload_to='post_images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Sport', 'Sport'), ('Entertainment', 'Entertainment'), ('Politics', 'Politics'), ('Education', 'Education'), ('Health', 'Health'), ('Business', 'Business')], max_length=25)),
                ('approve', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
