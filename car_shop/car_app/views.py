from django.shortcuts import render, get_object_or_404
from .models import Car, Store, Order

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_app/car_list.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car_app/car_detail.html', {'car': car})

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'car_app/store_list.html', {'stores': stores})
    
def order_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        customer_name = request.POST['customer_name']
        customer_email = request.POST['customer_email']
        total_price = car.price * quantity
        order = Order(car=car, quantity=quantity, total_price=total_price, customer_name=customer_name, customer_email=customer_email)
        order.save()
        return render(request, 'car_app/order_confirmation.html', {'order': order})
    else:
        return render(request, 'car_app/order_car.html', {'car': car})

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Cart, CartItem
from .forms import AddToCartForm

def add_to_cart(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    form = AddToCartForm(request.POST or None)
    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(car=car, cart=cart, defaults={'quantity': quantity})
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        return render(request, 'car_app/add_to_cart.html')
    return render(request, 'car_app/car_detail.html', {'car': car, 'form': form})

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect('home')
            cars = Car.objects.all()
            return render(request, 'car_app/car_list.html', {'cars': cars})

    else:
        form = CustomUserCreationForm()

    return render(request, 'car_app/registration/signup.html', {'form': form})

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomAuthenticationForm

# def login_view(request):
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = CustomAuthenticationForm()

#     return render(request, 'car_app/registration/login.html', {'form': form})

# views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        # Login prosedurunu icra edin
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('car_list')  # istifadəçi daxil olduqdan sonra profil səhifəsinə yönləndir
        else:
            # İstifadəçi mövcud deyil və ya şifrə yanlışdır, xəbərdarlıq göstər
            return render(request, 'car_app/registration/login.html')

    return render(request, 'car_app/registration/login.html')


# views.py
# from django.contrib.auth.views import PasswordChangeView
# from django.urls import reverse_lazy

# class MyPasswordChangeView(PasswordChangeView):
#     template_name = 'car_app/registration/password_change_form.html'
#     success_url = reverse_lazy('password_change_done')

# views.py

from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change')

    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed successfully.')
        return super().form_valid(form)

# views.py
from django.shortcuts import render

def profile_view(request):
    return render(request, 'car_app/profile.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('car_list')

# views.py

from django.shortcuts import render
from django.db.models import Q
from .models import Car

def search_view(request):
    query = request.GET.get('q')
    results = None

    if query:
        results = Car.objects.filter(Q(model__icontains=query) | Q(description__icontains=query))

    return render(request, 'car_app/search_results.html', {'results': results, 'query': query})
