from django.urls import path
from . import views
# from .views import add_to_cart
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Digər URL patternləri
]


urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('stores/', views.store_list, name='store_list'),
    # path('order/<int:car_id>/', views.order_car, name='order_car'),
    # path('add_to_cart/<int:car_id>/', add_to_cart, name='add_to_cart'),
    path('add_to_cart/<int:car_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='car_app/registration/login.html'), name='login'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('search/', search_view, name='search_view'),
]
