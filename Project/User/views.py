from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm


# A simple class based view
class HomeView(View):
    def get(self, request):
        return render(request, 'User/home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')  
            last_name = form.cleaned_data.get('last_name')  
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')  
            
            user = User.objects.create_user(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
            )
            user.set_password(password)
            user.save()
            return redirect('login')


    else:
        form = UserRegisterForm()
    return render(request, 'User/register.html', {'form':form})


def user_profile(request, user_username):
    user = get_object_or_404(User, username = user_username)
    if user.is_authenticated and user == request.user:
        return render(request, 'User/userprofile.html', {'user':user})
    else:
        return redirect('login')


class UserPasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'User/change-password.html'
    success_url = '/User/login/'