from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import BronzeCoupon, Earning, Profile, SilverCoupon, GoldCoupon, UltimateCoupon, DiamondCoupon


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput())
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BronzeCouponForm(forms.ModelForm):

    class Meta:
        model = BronzeCoupon
        fields = ['coupon_code', 'guider']


class SilverCouponForm(forms.ModelForm):

    class Meta:
        model = SilverCoupon
        fields = ['coupon_code', 'guider']


class GoldCouponForm(forms.ModelForm):

    class Meta:
        model = GoldCoupon
        fields = ['coupon_code', 'guider']


class DiamondCouponForm(forms.ModelForm):

    class Meta:
        model = DiamondCoupon
        fields = ['coupon_code', 'guider']


class UltimateCouponForm(forms.ModelForm):

    class Meta:
        model = UltimateCoupon
        fields = ['coupon_code', 'guider']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user', 'profile_created']


class WithdrawalForm(forms.ModelForm):
    withdraw = forms.CharField()

    class Meta:
        model = Earning
        fields = ['withdraw']
