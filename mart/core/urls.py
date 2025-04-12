from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('cart/', views.cart, name='cart'),
    path('account/', views.account, name='account'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('categories/', views.categories, name='categories'),
    path('partners/', views.partners, name='partners'),
    path('support/', views.support, name='support'),
    path('contactus/', views.contactus, name='contactus'),
    path('faqs/', views.faqs, name='faqs'),
    path('shipping_policy/', views.shipping_policy, name='shipping_policy'),
    path('refunds_policy/', views.returns_funds, name='refunds_policy'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    
    #accounts
    path('users/dashboard/', views.dashboard, name='dashboard'),
    path('users/account-details/', views.account_details, name='account-details'),
    path('users/my-orders/', views.my_orders, name='my-orders'),
    path('users/my-reviews/', views.my_reviews, name='my-reviews'),
    path('users/settings/', views.settings, name='settings'),
    path('users/whishlist/', views.whishlist, name='whishlist'),
    path('users/billing/', views.billing, name='billing'),
]