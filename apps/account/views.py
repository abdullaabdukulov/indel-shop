from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from .forms import LoginForm, RegisterForm
# from django.template import RequestContext
# from .models import Customer
# from django.contrib import messages



# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(
#                 request,
#                 username=data['username'],
#                 password=data['password']
#             )
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('shop:home')
#     else:
#         form = LoginForm()
#     return render(request, 'signin.html', {'form': form})


# def user_register(request):
#     if request.method == 'POST':
#         form  = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             messages.success(request, 'User registration successful')
#             Customer.objects.create(
                
#             )
           
            
#             return redirect('account:login')

#     else:
#         user_form = RegisterForm()

#     return render(request, 'signup.html', {'user_form': user_form})
        

def error_404_view(request, exception):
    return render(request, '404.html')