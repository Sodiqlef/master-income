from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('sponsored-post', views.sponsored_post_home, name='sponsored-post-home'),
    path('vendors/', views.coupon_vendors, name='vendors'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('package/', views.package, name='package'),
    path('advertise/', views.advertise, name='advertise'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_condition'),
    path('post/create', views.create_post, name='create_post'),
    path('support/form', views.support_form, name='support_form'),
    path('category/business', views.business, name='business'),
    path('category/sport', views.sport, name='sport'),
    path('category/entertainment', views.entertainment, name='entertainment'),
    path('category/politics', views.politics, name='politics'),
    path('category/health', views.health, name='health'),
    path('category/education', views.education, name='education'),

    #RegEx Path
    re_path(r'sponsored-post/(?P<pk>\d+)/', views.sponsored_post_news, name='sponsored-post-news'),
    re_path(r'post/(?P<pk>\d+)/', views.post, name='post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)