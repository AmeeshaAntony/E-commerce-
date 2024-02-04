from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderedItem
from products.models import Product
from customers.models import Customer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
@login_required(login_url='account')
def show_cart(request):
    user = request.user
    customer = user.customer_profile

    cart_obj, created = Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context = {'cart': cart_obj}
    return render(request, 'cart.html', context)

@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        print(quantity)

        cart_obj,created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )

        # Ensure quantity and product_id are valid numeric values
        try:
            quantity = int(quantity)
            product_id = int(product_id)
        except ValueError:
            return render(request, 'error.html', {'message': 'Invalid quantity or product ID'})

        product = get_object_or_404(Product, pk=product_id)
        ordered_item = OrderedItem.objects.create(
            product=product,
            owner=cart_obj,
            quantity=quantity
        )
        
        return redirect('cart')

    # Handle cases where it's not a POST request
    return render(request, 'cart_container.html')

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(OrderedItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


# views.py

def checkout_cart(request):
    if request.POST:
        try:
            user = request.user
            customer = user.customer_profile
            total = float(request.POST.get('total'))

            order_obj= Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.total_price=total
                order_obj.save()
                status_message = "Processed"
                messages.success(request, status_message)
            else:
                status_message = "Unable"
                messages.error(request, status_message)
        except Exception as e:
            status_message = "Unable"
            messages.error(request, status_message)

    return redirect('cart')
    return render(request, 'cart_container.html')

@login_required(login_url='account')
def view_orders(request):
    user=request.customer
    customer=user.customer_profile
    return render(request, 'cart.html', context)

'''def show_orders(request):
    user=request.customer
    customer=user.customer_profile
    all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':all_orders}
    return render(request, 'orders.html', context)'''