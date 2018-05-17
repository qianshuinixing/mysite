from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from account.forms import LoginForm, RegistrationForm, UserProfileForm


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        print(user_form)
        print("user验证：", user_form.is_valid())
        print(userprofile_form)
        print("profile验证：", userprofile_form.is_valid())
        if user_form.is_valid() and userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            new_userprofile = userprofile_form.save(commit=False)
            new_userprofile.user = new_user
            new_userprofile.save()
            return HttpResponse("成功")
        else:
            return render(request, "account/register2.html", {"form":user_form, "profile":userprofile_form})
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register2.html", {"form": user_form, "profile":userprofile_form})

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            # 验证是否是本网站的用户
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                return HttpResponse("欢迎，欢迎，你已经成功登录了")
            else:
                return HttpResponse("用户名或者密码错误")
        else:
            return HttpResponse("无效的登录")
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'account/login.html', {"login_form": login_form})

def user_logout(request):
    return HttpResponse("退出登录！")