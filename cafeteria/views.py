from django.shortcuts import render, redirect
from django.db.models import Count, Q
from cafeteria.models import Category, FoodItem, Order, OrderItem
from cafeteria.forms import OrderForm, QuantityForm

# Create your views here.
def menu(request):
    categories = Category.objects.prefetch_related("food_items")
    return render(request, "menu.html", {"categories": categories})


def home(request):
    categories = Category.objects.all()

    # Most ordered 4 items
    popular = (
        FoodItem.objects
        .annotate(order_count=Count('order_items'))
        .order_by('-order_count', '-food_price')[:4]
    )

    return render(request, 'home.html', {
        'categories': categories,
        'popular': popular,
    })


def order(request):
    categories = Category.objects.prefetch_related("food_items").all()
    all_items = [item for cat in categories for item in cat.food_items.all()]

    if request.method == 'POST':
        order_form = OrderForm(request.POST, request=request)
        qty_form = QuantityForm(request.POST, food_items=all_items)
    else:
        order_form = OrderForm(request=request)
        qty_form = QuantityForm(food_items=all_items)

    if request.method == 'POST' and order_form.is_valid() and qty_form.is_valid():
        # Create the order but don't save yet
        order = Order(order_status='Pending')

        if request.user.is_authenticated:
            # attach the logged-in user
            order.user = request.user

            order.customer_name = request.user.get_full_name() or request.user.username
            order.customer_id = getattr(request.user, "student_id", "")  # if you added it
        else:
            order.customer_name = order_form.cleaned_data.get("customer_name", "")
            order.customer_id = order_form.cleaned_data.get("customer_id", "")

        order.save()

        for item in all_items:
            qty = qty_form.cleaned_data.get(f'qty_{item.food_item_id}', 0)
            if qty and qty > 0:
                OrderItem.objects.create(order=order, food_item=item, quantity=qty)

        return redirect('order_success')

    return render(request, 'order.html', {
        'categories': categories,
        'order_form': order_form,
        'qty_form': qty_form,
    })


def order_success(request):
    return render(request, "order_success.html")