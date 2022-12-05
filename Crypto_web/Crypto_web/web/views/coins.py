
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from Crypto_web.common.validators import validate_coin, validate_coin_converter_all
from Crypto_web.web.forms import CreateCoinForm, ConvertCoinForm, \
    WithdrawAllCoinConvertedForm
from Crypto_web.web.models import Coin, Deposit


class CreateCoinView(views.CreateView):
    form_class = CreateCoinForm
    template_name = 'web/coins/coin_create.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UpdateCoinView(views.UpdateView):
    _current = 0
    model = Coin
    fields = ('quantity', 'wallet_address',)
    template_name = 'web/coins/coin_edit.html'
    success_url = reverse_lazy('index')
    context_object_name = 'coin'

    def get_queryset(self):
        return super().get_queryset()

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        current_value = UpdateCoinView._current
        if current_value == float(self.request.POST['quantity']):
            return redirect('coin withdrawal', self.kwargs['pk'])
        request.POST['quantity'] = str(UpdateCoinView._current - float(self.request.POST['quantity']))
        return super(UpdateCoinView, self).post(request, **kwargs)

    def get_context_data(self, **kwargs):
        UpdateCoinView._current = self.object.quantity
        return super().get_context_data()


class WithdrawAllCoinView(views.DeleteView):
    model = Coin
    http_method_names = ['delete']

    def dispatch(self, request, *args, **kwargs):
        handler = getattr(self, 'delete')
        return handler(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('dashboard')


class WithdrawAllConvertedCoinView(views.UpdateView):
    _currentPK = 0
    _coinPK = 0
    model = Coin
    form_class = WithdrawAllCoinConvertedForm
    template_name = 'web/coins/convert-withdrawall-coin.html'
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        new = kwargs['pk']
        WithdrawAllConvertedCoinView._currentPK = new
        kwargs = super().get(request, new)
        return kwargs

    def get_queryset(self):
        self.kwargs['pk'] = WithdrawAllConvertedCoinView._currentPK
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        return super().get_context_data()

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        coins = list(Coin.objects.filter(user_id=self.request.user.profile.user_id))
        validate_coin_converter_all(coins, request.POST, self.kwargs['pk'])

        return super(WithdrawAllConvertedCoinView, self).post(validate_coin_converter_all, **kwargs)

    def get_success_url(self):
        return reverse_lazy('updated deposit coin all', kwargs={'pk': self.object.pk})


class ConvertCoinView(views.UpdateView):
    _current = 0
    _convertedALL = 0
    model = Coin
    form_class = ConvertCoinForm
    template_name = 'web/coins/coin_convert.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'coin'

    def get_queryset(self):
        return super().get_queryset()

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        coins = list(Coin.objects.filter(user_id=self.request.user.profile.user_id))
        deposits = list(Deposit.objects.filter(user_id=self.request.user.profile.user_id))
        if not deposits:
            return redirect('fiat wallet')

        if validate_coin(coins, request.POST, self.kwargs['pk']) == 'False':
            ConvertCoinView._convertedALL = self.kwargs['pk']
            return redirect('custom withdrawal all coin', self.kwargs['pk'])

        return super(ConvertCoinView, self).post(validate_coin, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data()

    def get_success_url(self):
        return reverse_lazy('update deposit', kwargs={'pk': self.object.pk})
