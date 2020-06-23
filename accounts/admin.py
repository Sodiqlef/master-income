from django.contrib import admin
from .models import CouponCode, Withdrawal, Profile, Earning, PaymentStatus

# Register your models here.
admin.site.register(CouponCode)
admin.site.register(Withdrawal)
admin.site.register(Profile)
admin.site.register(Earning)
admin.site.register(PaymentStatus)




