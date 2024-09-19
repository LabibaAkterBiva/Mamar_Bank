from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView ,UserUpdateView
# UserBankAccountUpdateView
from.import views 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserUpdateView.as_view(), name='profile' ),
    path('change-password/', views.change_pass, name='change_password')
]