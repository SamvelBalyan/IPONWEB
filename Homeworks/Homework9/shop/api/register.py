import json

from django.shortcuts import render, redirect
from django.contrib import messages

from ..models.Customer import Customer
from ..models.MyCart import MyCart

from ..form import RegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect('home_n')
    else:
        form = RegisterForm()

        if request.method == 'POST':
            try:
                form = RegisterForm(json.loads(request.body))
                # print(json.loads(request.body))
            except:
                form = RegisterForm(request.POST)
                # print(request.POST)

            if form.is_valid():
                user = form.save()
                customer = Customer(user=user)
                customer.save()
                cart = MyCart(user=user)
                cart.save()
                messages.success(request, 'Account successfully created!' )
                return redirect('login')
            # else:
                # message if user is already registered
                # if form.password1 != form.password2:
                    # messages.info(request, "Passwords don't match")
                

        context={"form":form}
        return render(request, 'register.html', context)
