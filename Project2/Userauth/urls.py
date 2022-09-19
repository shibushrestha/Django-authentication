from django.urls import path, re_path
from . import views
from .views import Login, UserRegister
from django.contrib.auth.views import LogoutView

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    #re_path(r'^register/', views.register, name='register'),
    re_path(r'^register/', UserRegister.as_view(), name='register'),

    re_path(r'^login/', Login.as_view(), name='login'),
    re_path(r'^logout/', LogoutView.as_view(template_name='Userauth/logout.html'), name='logout'),
    re_path(r'^(?P<user_username>[a-zA-Z0-9@!#_.]+)/$', views.userprofile , name='user-profile'),
]
