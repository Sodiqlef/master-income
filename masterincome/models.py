import cloudinary
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


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
        return self.username


class SponsoredPost(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    feature_image = models.ImageField(upload_to='feature_image', null=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title



