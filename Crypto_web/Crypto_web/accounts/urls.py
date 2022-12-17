from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from Crypto_web.accounts.views import UserRegisterView, UserLoginView, ProfileView, UserLogOutView, delete_profile, \
    EditProfileView, BalanceAvailableView, ChangeUserPasswordView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='create profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
    path('balance/', BalanceAvailableView.as_view(), name='balance'),

    path('profile/<int:pk>/', ProfileView.as_view(), name='profile page'),
    path('profile/delete/<int:pk>/', delete_profile, name='delete profile page'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='profile edit'),


    path('password-change/', ChangeUserPasswordView.as_view(), name='edit password'),
    path('password_change_done', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done')


)












import Crypto_web.accounts.signals