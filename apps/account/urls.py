from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('add-address/', views.add_address, name='add-address'),
    # path('address-list/', views.address_list, name='address-list'),
    # path('edit-address/<int:pk>/', views.edit_address, name='edit-address'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
    #      name='password-reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    #      name='password-reset-done'),
    # path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    #      name='password-reset-confirm'),
    ]

