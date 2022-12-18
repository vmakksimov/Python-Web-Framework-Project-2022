from django.urls import path

from Crypto_web.web.views.coins import CreateCoinView, UpdateCoinView, WithdrawAllCoinView, ConvertCoinView, \
    WithdrawAllConvertedCoinView
from Crypto_web.web.views.contact_us import CreateContactView
from Crypto_web.web.views.fiatwallet import CreateDepositView, UpdateDepositView, WithdrawAllFiatView, \
    CustomWithdrawalFiatView, AlreadySetUpFiatWallet, UpdateDepositForCoinView
from Crypto_web.web.views.generic import HomeView, DashboardView, CryptoWalletView, FiatWalletView, \
    CryptoOverView, FiatWalletOverView, InboxView, AboutView

from Crypto_web.web.views.inbox import MessageView, MessageSentView, MessageDeleteView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create-coin/', CreateCoinView.as_view(), name='create coin'),
    path('contact/', CreateContactView.as_view(), name='contact'),
    path('fiatwallet/', FiatWalletView.as_view(), name='fiat wallet'),
    path('fiatwallet/setup/', CreateDepositView.as_view(), name='create deposit'),
    path('fiatwallet/done/', AlreadySetUpFiatWallet.as_view(), name='fiat wallet is ready'),
    path('about/', AboutView.as_view(), name='about'),


    path('inbox/', InboxView.as_view(), name='inbox'),
    path('inbox/message/<int:pk>/', MessageView.as_view(), name='user message'),
    path('inbox/message-sent/', MessageSentView.as_view(), name='message sent'),
    path('inbox/message-delete/<int:pk>/', MessageDeleteView.as_view(), name='message delete'),


    path('cryptowallet/<int:pk>/', CryptoWalletView.as_view(), name='crypto wallet'),
    path('overview/crypto/<int:pk>/', CryptoOverView.as_view(), name='overview crypto'),
    path('overview/crypto-withdrawal/partial/<int:pk>/', UpdateCoinView.as_view(), name='update coin'),
    path('overview/coin-withdrawal/<int:pk>/', WithdrawAllCoinView.as_view(), name='coin withdrawal'),
    path('overview/crypto-convert/<int:pk>/', ConvertCoinView.as_view(), name='coin convert'),
    path('overview/crypto-withdrawal/all/<int:pk>/', WithdrawAllConvertedCoinView.as_view(), name='custom withdrawal all coin'),

    path('overview/fiat/<int:pk>/', FiatWalletOverView.as_view(), name='overview fiat'),
    path('overview/fiat-update/<int:pk>/', UpdateDepositView.as_view(), name='update deposit'),
    path('overview/fiat-withdrawal/<int:pk>/', WithdrawAllFiatView.as_view(), name='fiat withdrawal'),
    path('overview/fiat-withdrawal/partial/<int:pk>/', CustomWithdrawalFiatView.as_view(), name='fiat withdrawal custom'),


    path('overview/updated-deposit-coin/<int:pk>/', UpdateDepositForCoinView.as_view(), name='updated deposit coin all'),

)

import Crypto_web.accounts.signals