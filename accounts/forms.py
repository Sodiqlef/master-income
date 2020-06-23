from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CouponCode, Withdrawal, Earning, Profile


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput())
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class CouponCodeForm(forms.ModelForm):

    class Meta:
        model = CouponCode
        fields = ['coupon_code', 'guider']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user', 'profile_created']


class WithdrawalForm(forms.ModelForm):

    class Meta:
        model = Withdrawal
        fields = ['activities_earning_to_withdraw', 'guider_bonus_to_withdraw']