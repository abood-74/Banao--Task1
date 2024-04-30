from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, User
from django.contrib.auth import authenticate, login
from django.views import View

class SignUp(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})
    
    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'accounts/signup.html', {'form': form})

class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                error_message = 'Invalid credentials. Please try again.'
                form.add_error(None, error_message)
        return render(request, 'accounts/login.html', {'form': form})

class DashBoard(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            print(user.first_name)
            return render(request, 'accounts/dashboard.html', {'user': user})
