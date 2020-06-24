from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, CouponVendor, User, SponsoredPost
from django.contrib import messages
from .forms import PostForm, SupportForm
from accounts.models import Earning, CouponCode
from django.db.models import Count
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    post_count = Post.objects.filter(approve=True).count()
    user_count = User.objects.count()
    queryset = Post.objects.filter(approve=True).order_by('-date').annotate(all=Count('approve'))
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if request.user.is_authenticated:
        last_login = int(datetime.now().strftime('%Y%m%d'))
        earned, boolCreate = Earning.objects.update_or_create(user=request.user)
        earning = Earning.objects.get(user=request.user)

        if last_login > earning.last_login:
            earning.daily_login +=30
            new, booleanCreate = Earning.objects.update_or_create(user=request.user, defaults={'last_login':last_login,
                                                                                               'daily_login': earning.daily_login})

    return render(request, 'home.html', {'posts': posts,
                                         'post_count': post_count,
                                         'user_count': user_count})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        coupon = CouponCode.objects.all()
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            if request.user.is_superuser:
                post.approve = True
            for each in coupon:
                if each.user == request.user:
                    post.save()
                    messages.success(request, 'Post created successfully waiting for approval')
                    return redirect('home')

            else:
                messages.error(request, 'Please activate your account first')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


def coupon_vendors(request):
    vendors = CouponVendor.objects.all()
    return render(request, 'vendors.html', {'vendors': vendors})


def support_form(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            messages.success(request, 'Form has been submitted, we will get back to you shortly.')
            return redirect('home')
    else:
        form = SupportForm()
    return render(request, 'support_form.html', {'form': form})


@login_required
def sponsored_post_home(request):
    sponsored_post = SponsoredPost.objects.all()
    return render(request, 'sponsored_post_home.html', {'sponsored_post': sponsored_post})


@login_required
def sponsored_post_news(request, pk):
    sponsored_post = get_object_or_404(SponsoredPost, pk=pk)
    earning = Earning.objects.all()
    if sponsored_post.pk > sponsored_post.post_pk:
        sponsored_post.post_pk = sponsored_post.pk
        request.user.earning.activities_earning += 100
        request.user.earning.save()
    return render(request, 'sponsored_post_news.html', {'sponsored_post': sponsored_post})


def post(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    coupon = CouponCode.objects.all()
    if request.user.is_authenticated:
        for each in coupon:
            if posts.created_by is not request.user.is_superuser:
                if request.user.date_joined < posts.date:
                    if request.user == each.user:
                        earning = Earning.objects.get(user=request.user)
                        if f'{posts.pk}' not in earning.news_pk:
                            earning.news_pk += f'{posts.pk}-'
                            earning.news_earned += 2
                            earning.save()
                            print(request.user.last_login)
    return render(request, 'news.html', {'posts': posts})


def business(request):
    queryset = Post.objects.filter(category='Business', approve=True).order_by('-date').annotate(all=Count('approve'))
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'post': post})


def politics(request):
    queryset = Post.objects.filter(category='Politics', approve=True).order_by('-date').annotate(all=Count('approve'))
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'post': post})


def entertainment(request):
    queryset = Post.objects.filter(category='Entertainment', approve=True).order_by('-date').annotate(all=Count('approve'))
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'post': post})


def sport(request):
    queryset = Post.objects.filter(category='Sport', approve=True).order_by('-date').annotate(all=Count('approve'))
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'post': post})


def health(request):
    queryset = Post.objects.filter(category='Health', approve=True).order_by('-date').annotate(all=Count('approve'))
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'post': post})


def education(request):
    queryset = Post.objects.filter(category='Education', approve=True).order_by('-date').annotate(all=Count('approve'))
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'post': post})


def disclaimer(request):
    return render(request, 'disclaimer.html')


def advertise(request):
    return render(request, 'advertise.html')


def package(request):
    return render(request, 'package.html')


def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')