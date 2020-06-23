from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=11, unique=True)
    profile_picture = models.ImageField(upload_to='images/', null=True)
    facebook_link = models.URLField(unique=True)
    account_name = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=20)
    profile_created = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


class CouponCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='coupon')
    coupon_code = models.CharField(max_length=20, unique=True)
    guider = models.CharField(max_length=150, default='none')
    is_activated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


class Earning(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='earning')
    daily_login = models.PositiveIntegerField(default=0)
    news_earned = models.IntegerField(default=0)
    approved_post = models.PositiveIntegerField(default=0)
    activities_earning = models.IntegerField(default=0)
    guider_bonus = models.IntegerField(default=0)
    activities_earning_withdrawn = models.IntegerField(default=0)
    activities_earning_remain = models.IntegerField(default=0)
    guider_bonus_withdrawn = models.IntegerField(default=0)
    guider_bonus_remain = models.IntegerField(default=0)
    last_login = models.IntegerField(default=20200000)
    post_pk = models.PositiveIntegerField(default=0)
    news_pk = models.TextField(null=True)

    def __str__(self):
        return f'{self.user}'


class Withdrawal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='withdrawal')
    facebook_link = models.URLField()
    account_details = models.TextField()
    activities_earning_to_withdraw = models.PositiveIntegerField(null=True)
    guider_bonus_to_withdraw = models.PositiveIntegerField(null=True)
    withdrawn = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


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
        return f'{self.user}'





