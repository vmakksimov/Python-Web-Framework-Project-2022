from django.urls import path

from Crypto_web.accounts.views import UserRegisterView, UserLoginView, ProfileView, UserLogOutView, delete_profile, \
    EditProfileView, BalanceAvailableView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='create profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
    path('balance/', BalanceAvailableView.as_view(), name='balance'),

    path('profile/<int:pk>/', ProfileView.as_view(), name='profile page'),
    path('profile/delete/<int:pk>/', delete_profile, name='delete profile page'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='profile edit'),


)

import Crypto_web.accounts.signals