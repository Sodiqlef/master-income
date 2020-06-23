from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    categories = (
        ('Sport', 'Sport'),
        ('Entertainment', 'Entertainment'),
        ('Politics', 'Politics'),
        ('Education', 'Education'),
        ('Health', 'Health'),
        ('Business', 'Business')
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    post = models.TextField()
    post_image = models.ImageField(upload_to='post_images/', null=True)
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
    name = models.CharField(max_length=100)
    subject = models.TextField()

    def __str__(self):
        return self.name


class SponsoredPost(models.Model):
    title = models.CharField(max_length=255)
    subject = models.TextField()
    feature_image = models.ImageField(upload_to='sponsored_image')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title