# appname/views.py
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import  RegistrationForm
from .models import  UserProfile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import CartItem

def user_login(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, "You already logged in.")
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "welcome ,you have logged in successfully .")

                return redirect('home')
            else:
                pass
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Success, You Logged Out Successfully.")
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.data["email"]
            password = form.data["password"]
            fname = form.data["fname"]
            lname = form.data["lname"]

            # Check if user with the given email already exists
            user_exists = UserProfile.objects.filter(email=email).exists()

            if not user_exists:
                # Create and save the User model instance
                new_user = User.objects.create_user(first_name=fname, last_name=lname, username=email, email=email,
                                                    password=password, is_active=True)
                messages.add_message(request, messages.SUCCESS, "hurrey , you successfully created account.")

                # Create and save the UserProfile model instance
                user_profile = UserProfile(fname=fname, lname=lname, password=password, email=email)
                user_profile.save()

                return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {"form": form})


@login_required(login_url='login')  
def home(request):
    if request.user.is_superuser:
        return redirect('home')
    else:
        user_id = request.user
        print(user_id)
        user = get_object_or_404(UserProfile, email=user_id)
        username = user.fname
        return render(request, 'home.html', { "username": username})

class CartListView(View):
    def get(self, request):
        user = request.user
        cart_items = CartItem.objects.filter(user=user)
        return render(request, 'cart.html', {'cart_items': cart_items})


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, "cart.html", {"cart_items": cart_items})
@login_required
def add_to_cart(request):
    if request.method == "POST":
        product_name = request.POST["product_name"]
        quantity = int(request.POST["quantity"])
        user = request.user
        cart_item, created = CartItem.objects.get_or_create(
            user=user, product=product_name, defaults={"quantity": quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
    return redirect("cart")

@login_required
def remove_from_cart(request, item_id):
    
    if request.method == "POST":
        try:
            cart_item = CartItem.objects.get(pk=item_id)
            cart_item.delete()
        except CartItem.DoesNotExist:
            pass
    return redirect("cart")

def about(request):
    return render(request, 'about.html')
