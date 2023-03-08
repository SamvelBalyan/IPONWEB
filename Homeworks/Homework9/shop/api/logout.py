from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import django.contrib.auth as auth

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')