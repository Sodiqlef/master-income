from django import forms
from .models import Support, SponsoredPost


class SupportForm(forms.ModelForm):

    class Meta:
        model = Support
        fields = ['username', 'email', 'phone_number', 'subject']

