from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# ---------------- SIGNUP ----------------
def signup_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'accounts/signup.html',
                {'error': 'Username already exists'}
            )

        User.objects.create_user(
            username=username,
            password=password
        )

        # ALWAYS go to login page
        return redirect('/accounts/login/')

    return render(request, 'accounts/signup.html')


# ---------------- LOGIN ----------------
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            # ALWAYS go to home page
            return redirect('/')

        return render(
            request,
            'accounts/login.html',
            {'error': 'Invalid username or password'}
        )

    return render(request, 'accounts/login.html')


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)

    # ALWAYS go to home page
    return redirect('/')
