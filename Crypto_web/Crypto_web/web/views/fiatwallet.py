
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from Crypto_web.web.forms import CreateDepositForm, ConvertFiatForm, WithdrawFiatForm

from Crypto_web.web.models import Coin, Deposit


class CreateDepositView(views.CreateView):
    form_class = CreateDepositForm
    template_name = 'web/fiatwallet/deposit_create.html'
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        deposits = list(Deposit.objects.filter(user_id=self.request.user.profile.user_id))
        if deposits:
            return redirect('fiat wallet is ready')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deposits = list(Deposit.objects.filter(user_id=self.request.user.profile.user_id))
        total_balance = sum([el.amount for el in deposits])

        context.update({
            'balance': total_balance,
        })

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class AlreadySetUpFiatWallet(views.TemplateView):
    template_name = 'web/fiatwallet/alreadysetup_fiatwallet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_context'] = True
        return context


class UpdateDepositView(views.UpdateView):
    _currentPK = 0
    _currentDeposit = 0
    _coinPK = 0
    _deletedCoin = 0
    model = Deposit
    form_class = ConvertFiatForm
    template_name = 'web/fiatwallet/deposit_edit.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'deposit'

    def get(self, request, *args, **kwargs):
        deposits = list(Deposit.objects.filter(user_id=self.request.user.profile.user_id))
        for el in deposits:
            current = el.id
            UpdateDepositView._coinPK = kwargs['pk']
            kwargs['pk'] = current
            break
        new = kwargs['pk']
        UpdateDepositView._currentPK = new
        kwargs = super().get(request, new)
        return kwargs

    def get_queryset(self):
        self.kwargs['pk'] = UpdateDepositView._currentPK
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        return super().get_context_data()

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        coins = list(Coin.objects.filter(user_id=self.request.user.profile.user_id))

        for coin in coins:
            if coin.id == UpdateDepositView._coinPK:
                amount = float(coin.fiat_value) + float(request.POST['amount'])
                new = str(round(amount, 4))
                request.POST['amount'] = new
                break

        return super(UpdateDepositView, self).post(request, **kwargs)

class UpdateDepositForCoinView(views.UpdateView):
    _currentPK = 0
    _currentDeposit = 0
    _coinPK = 0
    _deletedCoin = 0
    model = Deposit
    form_class = ConvertFiatForm
    template_name = 'web/fiatwallet/deposit_edit2.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'deposit'

    def get(self, request, *args, **kwargs):
        UpdateDepositForCoinView._deletedCoin = kwargs['pk']
        deposits = list(Deposit.objects.filter(user_id=self.request.user.profile.user_id))
        for el in deposits:
            current = el.id
            UpdateDepositForCoinView._coinPK = kwargs['pk']
            kwargs['pk'] = current

            break


        new = kwargs['pk']
        UpdateDepositForCoinView._currentPK = new
        kwargs = super().get(request, new)
        return kwargs

    def get_queryset(self):
        self.kwargs['pk'] = UpdateDepositForCoinView._currentPK
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        return super().get_context_data()

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        coins = list(Coin.objects.filter(user_id=self.request.user.profile.user_id))

        for coin in coins:
            if coin.id == UpdateDepositForCoinView._coinPK:
                amount = float(coin.fiat_value) + float(request.POST['amount'])
                new = str(round(amount, 4))
                request.POST['amount'] = new
                break

        return super(UpdateDepositForCoinView, self).post(request, **kwargs)

    def get_success_url(self):
        b = UpdateDepositForCoinView._deletedCoin
        return reverse_lazy('coin withdrawal', kwargs={'pk': b})

class CustomWithdrawalFiatView(views.UpdateView):
    _current = 0
    model = Deposit
    fields = ('amount', 'iban', 'beneficiary_name', 'currency',)
    template_name = 'web/fiatwallet/customer_withdrawal_fiat.html'
    success_url = reverse_lazy('index')
    context_object_name = 'deposit'

    def get_queryset(self):
        return super().get_queryset()

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        amount = list(Deposit.objects.filter(user_id=self.request.user.profile.user_id))
        a = CustomWithdrawalFiatView._current
        current_value = a
        if current_value == float(self.request.POST['amount']):
            return redirect('fiat withdrawal', self.kwargs['pk'])
        request.POST['amount'] = str(CustomWithdrawalFiatView._current - float(self.request.POST['amount']))
        return super(CustomWithdrawalFiatView, self).post(request, **kwargs)

    def get_context_data(self, **kwargs):
        CustomWithdrawalFiatView._current = self.object.amount
        return super().get_context_data()


class WithdrawAllFiatView(views.UpdateView):
    _current = 0
    model = Deposit
    form_class = WithdrawFiatForm
    template_name = 'web/fiatwallet/withdraw-fiat.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return super().get_queryset()

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        amount = sum(el.amount for el in Deposit.objects.filter(user_id=self.request.user.profile.user_id))
        if float(request.POST['amount']) != amount:
            return redirect('fiat withdrawal custom', self.kwargs['pk'])
        request.POST['amount'] = 0
        return super(WithdrawAllFiatView, self).post(request, **kwargs)

    def get_context_data(self, **kwargs):
        WithdrawAllFiatView._current = self.object.amount
        return super().get_context_data()



