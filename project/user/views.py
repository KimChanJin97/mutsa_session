from django.http import QueryDict
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserSignupForm, CustomUserSigninForm

# 회원가입
def signup_function(request):
    form = CustomUserSignupForm()
    if request.method == 'POST':
        form = CustomUserSignupForm(request.POST)
        # make_error = QueryDict.copy(request.POST)
        # make_error["username"] = ""
        # form = CustomUserSignupForm(make_error)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog:read_all")
    return render(request, "signup.html", {"form":form})

# 로그인
def signin_function(request):
    form = CustomUserSigninForm()
    if request.method == 'POST':
        form = CustomUserSigninForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("blog:read_all")
    return render(request, "signin.html", {"form":form})

# 로그아웃
def signout_function(request):
    logout(request)
    return redirect("blog:read_all")