from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import UserForm
from .forms import UserForm
from .models import User
from django.contrib import messages

def registerUser(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():

            # create the user using form
            # password = form.cleaned_data('password')
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # form.save()
            # create user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'your account has been register succefuly ')
            return redirect('registerUser')

        else:
            print("form invalid")
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)