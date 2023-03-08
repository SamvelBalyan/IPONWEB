from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..form import AvatarForm 

@login_required(login_url='login')
def change_avatar(request):
  if request.method == 'POST':
    form = AvatarForm(request.POST, request.FILES)
    if form.is_valid():
      avatar = form.cleaned_data['avatar']
      request.user.customer.avatar = avatar
      request.user.customer.save()
      return redirect('account')
  else:
    form = AvatarForm()
  return render(request, 'change_avatar.html', {'form': form})
