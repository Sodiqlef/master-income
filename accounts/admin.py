from django.contrib import admin
from .models import BronzeCoupon, PaymentStatus, Earning, Profile, SilverCoupon, GoldCoupon, UltimateCoupon, DiamondCoupon

# Register your models here.
admin.site.register(Profile)
admin.site.register(Earning)
admin.site.register(PaymentStatus)
admin.site.register(BronzeCoupon)
admin.site.register(SilverCoupon)
admin.site.register(GoldCoupon)
admin.site.register(DiamondCoupon)
admin.site.register(UltimateCoupon)






