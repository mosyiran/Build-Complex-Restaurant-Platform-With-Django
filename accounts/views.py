from lib2to3.fixes.fix_input import context

from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import UserForm
from vendor.forms import VendorForm
from vendor.models import Vendor
from .forms import UserForm
from .models import User, UserProfile
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


def registerVendor(request):
    if request.method == 'POST':
        # store the data
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.Vendor
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            user.profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user.profile
            messages.success(request, 'your account has been register succefuly ')
            return redirect('registerVendor')

        else:
            print("form invalid")
            print(form.errors)
    else:

       form = UserForm()
       v_form = VendorForm()

    context = {
        'form': form,
        'v_form': v_form,
    }
    return render(request, 'accounts/registerVendor.html', context)