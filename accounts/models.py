from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=11, unique=True)
    profile_picture = models.ImageField(upload_to='profile_picture')
    facebook_link = models.URLField(unique=True)
    account_name = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=20)
    profile_created = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


class SilverCoupon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='silver')
    coupon_code = models.CharField(max_length=20, unique=True)
    guider = models.CharField(max_length=150, default='none')
    is_activated = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.pk}   {self.user}'


class BronzeCoupon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bronze')
    coupon_code = models.CharField(max_length=20, unique=True)
    guider = models.CharField(max_length=150, default='none')
    is_activated = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user}'


class GoldCoupon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='gold')
    coupon_code = models.CharField(max_length=20, unique=True)
    guider = models.CharField(max_length=150, default='none')
    is_activated = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user}'


class UltimateCoupon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ultimate')
    coupon_code = models.CharField(max_length=20, unique=True)
    guider = models.CharField(max_length=150, default='none')
    is_activated = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user}'


class DiamondCoupon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='diamond')
    coupon_code = models.CharField(max_length=20, unique=True)
    guider = models.CharField(max_length=150, default='none')
    is_activated = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user}'


class Earning(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='earning')
    sponsored_post = models.IntegerField(default=0)
    daily_earning = models.IntegerField(default=0)
    withdrawal = models.CharField(max_length=100, null=True)
    guider_bonus = models.IntegerField(default=0)
    post_pk = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user} {self.pk}'


class PaymentStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='status')
    earnings_review = models.BooleanField(null=True)
    sponsored_post_verification = models.BooleanField(null=True)
    details_cross_check = models.BooleanField(null=True)
    last_payment_upload = models.BooleanField(null=True)
    deduction = models.BooleanField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    made = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user} {self.pk}'




