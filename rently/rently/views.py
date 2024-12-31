from django.shortcuts import render,redirect
from product.models import Product,Cart,Wishlist,Payment
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm, ForgotPasswordForm,ProductForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Form's save method already handles password hashing
            messages.success(request, 'Your account has been created!')
            return redirect('login')  # Redirect to login page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('product_view')
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Handle password reset logic here (you can use Django's built-in password reset view)
            messages.success(request, 'If the email exists, a password reset link will be sent.')
            return redirect('login')
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgot_password.html', {'form': form})


def product_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def cart_view(request):
    if request.method == 'GET' and 'add' in request.GET:
        product_id = request.GET.get('add')
        product = get_object_or_404(Product, id=product_id)
        
        # Get or create a cart for the current user
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        if product in cart.products.all():
            messages.info(request, "This product is already in your cart.")
        else:
            cart.products.add(product)
            messages.success(request, "Product added to cart!")
        return redirect('cart_view')  # Redirect to the cart view page

    # Display the cart items
    cart = Cart.objects.filter(user=request.user).first()
    context = {'cart': cart}
    return render(request, 'cart.html', context)


def wishlist_view(request):
    if request.method == 'GET' and 'add' in request.GET:
        product_id = request.GET.get('add')
        product = get_object_or_404(Product, id=product_id)
        
        # Get or create a wishlist for the current user
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        
        if product in wishlist.products.all():
            messages.info(request, "This product is already in your wishlist.")
        else:
            wishlist.products.add(product)
            messages.success(request, "Product added to wishlist!")
        return redirect('wishlist_view')  # Redirect to the wishlist view page

    # Display the wishlist items
    wishlist = Wishlist.objects.filter(user=request.user).first()
    context = {'wishlist': wishlist}
    return render(request, 'wishlist.html', context)

def payment_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')  # Redirect to login if user isn't authenticated

    rent_product_id = request.GET.get('rent', None)
    cart_payment = request.GET.get('cart', None)
    context = {}

    if rent_product_id:
        # Handle single product payment
        product = get_object_or_404(Product, id=rent_product_id)
        context['product'] = product

        if request.method == 'POST':
            # Create Payment instance for single product
            payment = Payment.objects.create(
                user=user,
                payment_price=product.product_price,
                payment_status='PENDING'
            )
            payment.products.add(product)
            payment.payment_status = 'COMPLETED'  # Mark as completed after payment processing
            payment.save()
            return redirect('product_view')  # Redirect after successful payment

        return render(request, 'payment.html', context)

    elif cart_payment:
        # Handle cart payment
        cart = Cart.objects.filter(user=user).first()
        if not cart or not cart.products.exists():
            return redirect('cart_view')  # Redirect if the cart is empty

        context['products'] = cart.products.all()
        context['total_price'] = sum([product.product_price for product in cart.products.all()])

        if request.method == 'POST':
            # Create Payment instance for cart
            total_price = sum([product.product_price for product in cart.products.all()])
            payment = Payment.objects.create(
                user=user,
                payment_price=total_price,
                payment_status='PENDING'
            )
            for product in cart.products.all():
                payment.products.add(product)
            payment.payment_status = 'COMPLETED'  # Mark as completed after payment processing
            payment.save()

            # Clear the cart after successful payment
            cart.products.clear()
            return redirect('product_view')  # Redirect after successful payment

        return render(request, 'payment_cart.html', context)

    return redirect('product_view')  # Fallback to product view if no specific payment

def product_detail_view(request, slug):
    product = get_object_or_404(Product, product_slug=slug)
    return render(request, 'product_detail.html', {'product': product})

def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.product_owner = request.user
            product.save()
            messages.success(request, "Product added successfully!")
            return redirect('product_list')  # Redirect to the product list page
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'add_product.html', context)


