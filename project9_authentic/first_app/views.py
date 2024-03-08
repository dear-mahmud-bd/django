from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm

# Create your views here.
def home(req):
    return render(req, './home.html')

def signup(req):
    if not req.user.is_authenticated:
        if req.method=='POST':
            form = RegisterForm(req.POST)
            if form.is_valid():
                messages.success(req, "Account created successfully")
                form.save(commit=True)
                # print(form.cleaned_data)
        else:
            form = RegisterForm()        
        return render(req, './signup.html', {'form':form})
    else:            
        return redirect('profile_page')


def signin(req):
    if not req.user.is_authenticated:
        if req.method=='POST':
            form = AuthenticationForm(request=req, data=req.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass) # check user exist or not in database
                if user is not None:
                    login(req, user)
                    return redirect('profile_page')
        else:
            form = AuthenticationForm()
        return render(req, './signin.html', {'form':form})
    else:            
        return redirect('profile_page')
        
         
def user_logout(req):
    logout(req)
    return redirect('signin_page')
    
     
def profile(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = ChangeUserData(req.POST, instance = req.user)
            if form.is_valid():
                messages.success(req, 'Account updated successfully')
                form.save()
                # print(form.cleaned_data)
        else:
            form = ChangeUserData(instance = req.user)
        return render(req, './profile.html', {'form': form})
    else:
        return redirect('signin_page')

    
def pass_change(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = PasswordChangeForm(user=req.user, data = req.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(req, form.user) # password update korbe
                return redirect('profile_page')
        else:
            form = PasswordChangeForm(user=req.user)
        return render(req, './passchng.html', {'form':form})
    else:
        return redirect('signin_page')
    
def pass_change_without(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = SetPasswordForm(user=req.user, data = req.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(req, form.user) # password update korbe
                return redirect('profile_page')
        else:
            form = SetPasswordForm(user=req.user)
        return render(req, './passchng.html', {'form':form})
    else:
        return redirect('signin_page')
    
    
def change_user_data(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = ChangeUserData(req.POST, instance = req.user)
            if form.is_valid():
                messages.success(req, 'Account updated successfully')
                form.save()
                # print(form.cleaned_data)
        else:
            form = ChangeUserData()
        return render(req, './profile.html', {'form': form})
    else:
        return redirect('signin_page')