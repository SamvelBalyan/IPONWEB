import json 

from django.shortcuts import render, redirect
from django.contrib import messages

import django.contrib.auth as auth


def login(request):
    if request.user.is_authenticated:
        return redirect('home_n')
    else:
        if request.method=='POST':
            try:
                log = json.loads(request.body).get('username')
                pas = json.loads(request.body).get('password')
            except:
                log = request.POST.get('username')
                pas = request.POST.get('password')

            user = auth.authenticate(request, username = log, password = pas)

            if user is not None:
                auth.login(request, user)
                return redirect('home_n')
            else:
                messages.info(request, "Username or password is incorrect")

        context={}
        return render(request, 'login.html', context)
