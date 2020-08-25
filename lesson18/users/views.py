from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, UpdateForm, UpdateUserIcon, UpdateGender
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def regform(request):

    if request.method == 'POST':
         rg = RegisterForm(request.POST)
         if rg.is_valid():

            rg.save()
            username = rg.cleaned_data.get('username')
            messages.success(request,f'Пользователь {user.username} был зарегистрирован')
            return redirect('mainpage')
    else:
        rg = RegisterForm()

    return render(request,'users/regform.html',{'rg':rg})

@login_required
def profile(request):

    if request.method == 'POST':
        updateIcon = UpdateUserIcon(request.POST,request.FILES,instance = request.user.profile)
        updetaUserform = UpdateForm(request.POST,instance = request.user)
        updateGender = UpdateGender(request.POST,instance = request.user.profile)
        if updateIcon.is_valid() and updetaUserform.is_valid() and updateGender.is_valid():
            updetaUserform.save()
            updateIcon.save()
            updateGender.save()
            messages.success(request,f'Ваш аккаунт был обновлен')
            return redirect('profile')
    else:
        updateIcon = UpdateUserIcon(instance = request.user.profile)
        updetaUserform = UpdateForm(instance = request.user)
        updateGender = UpdateGender(instance = request.user.profile)
    data = {
        'updateIcon':updateIcon,
        'updetaUserform':updetaUserform,
        'updateGender':updateGender,
    }
    return render(request,'users/profile.html',data)
