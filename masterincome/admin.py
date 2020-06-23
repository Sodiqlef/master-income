from django.contrib import admin
from masterincome.models import  Post, CouponVendor, Support, SponsoredPost

# Register your models here.
admin.site.register(Post)
admin.site.register(CouponVendor)
admin.site.register(Support)
admin.site.register(SponsoredPost)

