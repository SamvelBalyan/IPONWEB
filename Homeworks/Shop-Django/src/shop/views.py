from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import django.contrib.auth as auth
from .models import *
from .form import RegisterForm, AvatarForm
from django.contrib import messages
from django.shortcuts import get_object_or_404


#
def login(request):
    if request.user.is_authenticated:
        return redirect('home_n')
    else:
        if request.method=='POST':
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


#
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


#
def register(request):
    if request.user.is_authenticated:
        return redirect('home_n')
    else:
        form = RegisterForm()

        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                customer = Customer(user=user)
                customer.save()
                cart = MyCart(user=user)
                cart.save()
                messages.success(request, 'Account successfully created!' )
                return redirect('login')
            else:
                messages.info(request, "Passwords don't match")

        context={"form":form}
        return render(request, 'register.html', context)


#
@login_required(login_url='login')
def products(request):  
    
    products = Item.objects.all()    
    return render(request, 'home.html', {'products':products})


#
@login_required(login_url='login')
def categories(request):
    item_cat = ItemCategory.objects.all()
    store_cat = StoreCategory.objects.all()

    return render(request, "categories.html", {"store_cat":store_cat, "item_cat":item_cat})


#
@login_required(login_url='login')
def shops(request):
    stores = Store.objects.all()

    return render(request, "shops.html", {"stores":stores})


#
@login_required(login_url='login')
def owner(request,id):
    owner = StoreOwner.objects.get(id=id)

    owned_shops = Store.objects.filter(owner=owner)
    return render(request, 'owner.html', {"owner":owner, "owned_shops":owned_shops})


#
@login_required(login_url='login')
def customers(request):  return render(request, 'customers.html')


#
@login_required(login_url='login')
def show_item(request,id):
    item = Item.objects.get(id=id)
    return render(request, 'item.html', {"item":item})


#
@login_required(login_url='login')
def add_to_cart(request, id):
    item = Item.objects.get(id=id)
    cart, created = MyCart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        my_cart=cart,
        item=item
    )
    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
    cart_item.save()
    cart.save()

    return render(request, 'add_to_cart.html', {})


#
@login_required(login_url='login')
def account(request):
    customer = Customer.objects.get(user=request.user)
    cart = MyCart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(my_cart=cart)
    
    cont, total_cost=[], 0
    for item in cart_items:
        cont.append({'id':item.id,
                     'name':item.item.name,
                     'quantity':item.quantity,
                     'price':item.quantity*item.item.price})
        total_cost += item.quantity*item.item.price

    context = {'customer':customer, 'cart_items':cont, 'total_cost':total_cost}

    return render(request, 'account.html', context)


#
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


#
@login_required(login_url='login')
def delete_from_cart(request, id):
    item = get_object_or_404(CartItem, id=id)
    item.delete()
    return redirect('account')


#
@login_required(login_url='login')
def shop_view(request,id):
    shop = Store.objects.get(id=id)

    return render(request, 'shop_view.html', {'shop':shop})
