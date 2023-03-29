from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import CustomUserCreationForm, AddressForm
from .models import CustomAddress


def signup(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        address_form = AddressForm(request.POST)
        if user_form.is_valid() and address_form.is_valid():
            user = user_form.save(commit=False)
            user.is_active = True
            user.save()
            address = address_form.save(commit=False)
            address.save()
            custom_address = user.customaddress_set.create(address=address, is_default=True)
            login(request, user)
            return redirect('home')
    else:
        user_form = CustomUserCreationForm()
        address_form = AddressForm()
    return render(request, 'signup.html', {'user_form': user_form, 'address_form': address_form})


#
# @login_required
# def add_address(request):
#     if request.method == 'POST':
#         form = AddressForm(request.POST)
#         if form.is_valid():
#             address = form.save(commit=False)
#             address.save()
#             custom_address = CustomAddress(user=request.user, address=address)
#             custom_address.save()
#             messages.success(request, 'Your address has been added!')
#             return redirect('address-list')
#     else:
#         form = AddressForm()
#     return render(request, 'add_address.html', {'form': form})
#
#
# @login_required
# def address_list(request):
#     custom_addresses = CustomAddress.objects.filter(user=request.user)
#     return render(request, 'address_list.html', {'custom_addresses': custom_addresses})
#
#
# @login_required
# def edit_address(request, id):
#     custom_address = get_object_or_404(CustomAddress, id=id, user=request.user)
#     if request.method == 'POST':
#         form = AddressForm(request.POST, instance=custom_address.address)
#         if form.is_valid():
#             address = form.save()
#             custom_address.address = address
#             custom_address.save()
#             messages.success(request, 'Your address has been updated!')
#             return redirect('address-list')
#     else:
#         form = AddressForm(instance=custom_address.address)
#     return render(request, 'edit_address.html', {'form': form, 'custom_address': custom_address})
#
#
# @login_required
# def delete_address(request, id):
#     custom_address = get_object_or_404(CustomAddress, id=id, user=request.user)
#     custom_address.delete()
#     messages.success(request, 'Your address has been deleted!')
#     return redirect('address-list')
#
#
def login_view(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return HttpResponse("""
                <h1>You have successfully logged in!</h1>
            """)
            # return redirect('home')
        else:
            messages.error(request, 'Invalid phone number or password.')
    return render(request, 'signin.html')
#
#
# def logout_view(request):
#     logout(request)
#     messages.success(request, 'You have successfully logged out!')
#     return redirect('home')
