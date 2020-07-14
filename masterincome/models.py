import cloudinary
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    categories = (
        ('Sport', 'Sport'),
        ('Entertainment', 'Entertainment'),
        ('Politics', 'Politics'),
        ('Education', 'Education'),
        ('Health', 'Health'),
        ('Business', 'Business'),
        ('Other', 'Other')
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    post = models.TextField()
    post_image = CloudinaryField('post_image')
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=25, choices=categories)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class CouponVendor(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Support(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=11, null=True)
    subject = models.TextField()

    def __str__(self):
        return self.name


class SponsoredPost(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    feature_image = CloudinaryField('feature_image')
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title