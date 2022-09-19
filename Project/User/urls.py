from django.urls import path, re_path
from User import views
from User.views import UserPasswordChange
from django.contrib.auth import views as auth_views

app_name='User'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    re_path(r'^register/$', views.register_user, name='register'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='User/login.html'), name='login'),
    re_path(r'^(?P<user_username>[a-zA-Z0-9.@!_]+)/logout/$', auth_views.LogoutView.as_view(template_name='User/logout.html'),
        name='logout'),
    # take good look to this re_path
    re_path(r'^(?P<user_username>[a-zA-Z0-9.@!_]+)/$', views.user_profile, name='userprofile'),
    re_path(r'^(?P<user_username>[a-zA-Z0-9.@!_]+)/changepassword/$', UserPasswordChange.as_view(), name='changepassword'),
]
