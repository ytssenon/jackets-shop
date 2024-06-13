from django.shortcuts import render, redirect
from .models import Jacket, Cart


def home(request):
    jackets = Jacket.objects.all()
    cart_items = Cart.objects.all()
    total_quantity = sum(item.quantity for item in cart_items)
    total_cost = sum(item.total_price for item in cart_items)
    return render(request, 'jackets/home.html', {'jackets': jackets, 'total_quantity': total_quantity, 'total_cost': total_cost})

def add_to_cart(request, jacket_id):
    jacket = Jacket.objects.get(id=jacket_id)
    cart_item, created = Cart.objects.get_or_create(jacket=jacket)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('home')

def clear_cart(request):
    Cart.objects.all().delete()
    return redirect('home')
