from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import UserCreateForm, ProfileUpdateForm
from django.views import View
from django.contrib import messages


def homepage(request):
    return render(request, 'home.html')


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            'form': create_form
        }
        return render(request, 'register.html', context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect("home")
        else:
            context = {
                'form': create_form
            }
            return render(request, 'register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'signin.html', context)

    def post(self, request):

        signin_form = AuthenticationForm(data=request.POST)

        if signin_form.is_valid():
            user = signin_form.get_user()
            login(request, user)
            messages.success(request, 'you have successfully logged in')
            return redirect('home')

        else:
            return render(request, 'signin.html', {'signin_form': signin_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, 'you have succesfully logged out')
        return redirect('home')


class ProfileUpdate(View):
    def get(self, request):
        edit_form = ProfileUpdateForm(instance=request.user)
        context = {
            'edit_form': edit_form
        }
        return render(request, 'profile_update.html', context)

    def post(self, request):
        edit_form = ProfileUpdateForm(data=request.POST,

                                      instance=request.user,
                                      )

        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'you have succesfully updated your profile !')
            return redirect('home')
        else:
            context = {
                'edit_form': edit_form
            }
            return render(request, 'profile_update.html', context)
