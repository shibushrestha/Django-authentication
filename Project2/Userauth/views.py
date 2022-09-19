from django.shortcuts import get_object_or_404, render, redirect
from Userauth.forms import UserRegisterForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

def home(request):
    return render(request, 'Userauth/home.html',)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'Userauth/register.html', {'form':form})

# The equivalent classed-based view for the above register view(function-based view)
class UserRegister(CreateView):
    form_class = UserRegisterForm
    template_name = 'Userauth/register.html'
    success_url = '/Userauth/login/'


# The Login view
class Login(LoginView):
    template_name = 'Userauth/login.html'


# The user profile page
def userprofile(request, user_username):
    user = get_object_or_404(User, username = user_username)
    if user.is_authenticated and user == request.user:
        context = {'user':user}
        return render(request, 'Userauth/user-profile.html', context)
    else:
        return redirect('login')



