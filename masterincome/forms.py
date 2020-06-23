from django import forms
from .models import Post, Support, CouponVendor


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'post', 'post_image', 'category']


class SupportForm(forms.ModelForm):

    class Meta:
        model = Support
        fields = ['name', 'subject']