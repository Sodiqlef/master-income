from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, re_path


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('activate/bronze/', views.bronze_form, name='bronze_form'),
    path('activate/silver/', views.silver_form, name='silver_form'),
    path('activate/gold/', views.gold_form, name='gold_form'),
    path('activate/diamond/', views.diamond_form, name='diamond_form'),
    path('activate/ultimate/', views.ultimate_form, name='ultimate_form'),
    path('profile/form/', views.profile_form, name='profile_form'),
    path('payment/status/', views.payment_status, name='payment_status'),
    #path('withdraw/', views.withdrawal_form, name='withdrawal_form'),
    path('password/change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
         name='password_change'),
    path('password/change/done', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),

    path('reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html',
             email_template_name='password_reset_email.html',
             subject_template_name='password_reset_subject.txt'
         ),
         name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),

    path('reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    # RegEx Paths

    re_path(r'profile/', views.profile, name='profile'),
    re_path(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
            auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
            name='password_reset_confirm'),

]
