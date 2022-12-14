from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return redirect('shop:home')
    
    
#     return render(request, 'signin.html')


# def user_logout(request):
#     logout(request)
#     return redirect('shop:home')
    
# def user_register(request):
#     pass

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('shop:home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'signin.html', {'form': form})