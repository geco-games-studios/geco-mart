from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def cart(request):
    return render(request, 'cart.html')

def account(request):
    return render(request, 'account.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def categories(request):
    return render(request, 'categories.html')

def partners(request):
    return render(request, 'partners.html')

def support(request):
    return render(request, 'support.html')

def contactus(request):
    return render(request, 'contactus.html')

def faqs(request):
    return render(request, 'faqs.html')

def shipping_policy(request):
    return render(request, 'shipping-policy.html')

def returns_funds(request):
    return render(request, 'refund-policy.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')


#user-accounts
def dashboard(request):
    return render(request, 'users/dashboard.html')

def account_details(request):
    return render(request, 'users/account-details.html')

def my_orders(request):
    return render(request, 'users/my-orders.html')

def my_reviews(request):
    return render(request, 'users/my-reviews.html')

def settings(request):
    return render(request, 'users/settings.html')

def whishlist(request):
    return render(request, 'users/whishlist.html')

def billing(request):
    return render(request, 'users/billing.html')
