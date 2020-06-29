from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path
from .import views
urlpatterns=[
    path('signup-user/',views.SIgnupView,name="signup"),
    path('login/',views.LoginView,name="login"),
    path('logout/',views.Logout_view ,name="logout"),
    path('regular/',views.RegularView,name="regular"),
    path('organization/',views.OrganizationView,name="organization"),
    path('activate/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        views.activate, name='activate'),
    path('reset-password',
         PasswordResetView.as_view(template_name='user/password_reset_form.html'), name='password_reset'),
    path('reset-password/done',
         PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/',
         PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset-password/complete/',
    PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),

    path('dashboard/',views.Dashboard,name="dashboard"),
    path('post-media/',views.PostMedia,name="postmedia"),

]