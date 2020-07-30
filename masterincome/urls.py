from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.home, name='home'),
    path('sponsored-post', views.sponsored_post_home, name='sponsored-post-home'),
    path('vendors/', views.coupon_vendors, name='vendors'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('package/', views.package, name='package'),
    path('about-us/', views.about_us, name='about-us'),
    path('advertise/', views.advertise, name='advertise'),
    path('privacypolicy/', views.privacy_policy, name='privacypolicy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_condition'),
    path('support/form', views.support_form, name='support_form'),
    path('dashboard/', views.vendors_dashboard, name='vendors_dashboard'),


    #RegEx Path
    re_path(r'sponsored-post/(?P<pk>\d+)', views.sponsored_post_news, name='sponsored-post-news'),
]
handler404 = views.handler404
handler500 = views.handler500