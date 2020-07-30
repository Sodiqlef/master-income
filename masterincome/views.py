from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import CouponVendor, User, SponsoredPost
from django.contrib import messages
from .forms import SupportForm
from accounts.models import Earning, Profile
from django.db.models import Count
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def coupon_vendors(request):
    vendors = CouponVendor.objects.all()
    return render(request, 'vendors.html', {'vendors': vendors})


def support_form(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            support = form.save(commit=False)
            support.save()
            messages.success(request, 'Form has been submitted, we will get back to you shortly.')
            return redirect('home')
    else:
        form = SupportForm()
    return render(request, 'support_form.html', {'form': form})


@login_required
def sponsored_post_home(request):
    coupon = CouponCode.objects.all()
    sponsored_post = SponsoredPost.objects.all().order_by('-date')
    return render(request, 'sponsored_post_home.html', {'sponsored_post': sponsored_post,
                                                        'coupon': coupon})


@login_required
def sponsored_post_news(request, pk):
    coupon = CouponCode.objects.all()
    sponsored_post = get_object_or_404(SponsoredPost, pk=pk)
    earning = Earning.objects.get(user=request.user)
    if sponsored_post.pk > earning.post_pk:
        earning.post_pk = sponsored_post.pk
        earning.sponsored_post += 100
        earning.save()
    return render(request, 'sponsored_post_news.html', {'sponsored_post': sponsored_post})


def disclaimer(request):
    return render(request, 'disclaimer.html')


def advertise(request):
    return render(request, 'advertise.html')


def package(request):
    return render(request, 'package.html')


def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')


def privacy_policy(request):
    return render(request, 'privacypolicy.html')


def about_us(request):
    return render(request, 'about-us.html')


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


@login_required
def vendors_dashboard(request):
    return render(request, 'vendors_dashboard.html',
                  {'vendors': vendors, 'codes': codes})