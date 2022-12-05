
from django.views import generic as views
from Crypto_web.common.helpers import get_unique_object
from Crypto_web.web.models import Coin, Deposit, ContactUs


class HomeView(views.TemplateView):
    template_name = 'web/index2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_context'] = True

        return context


class AboutView(views.TemplateView):
    template_name = 'web/generic/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_context'] = True
        return context


class DashboardView(views.ListView):
    model = Coin
    template_name = 'web/generic/dashboard.html'
    context_object_name = 'coins'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coins = Coin.coin_prices_two.field.choices
        context['loop_times'] = range(len(coins))
        context.update({
            'coins': coins,

        })
        return context


class InboxView(views.ListView):
    model = ContactUs
    template_name = 'web/inbox/inbox.html'
    context_object_name = 'messages'
    paginate_by = 3

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a= 5
        messages = list(ContactUs.objects.filter(author_id=self.request.user.id))
        total_messages = len(messages)

        context.update({
            'messages': messages,
            'total_messages': total_messages,


        })
        return context


class CryptoOverView(views.ListView):
    model = Coin
    template_name = 'web/overview/crypto-overview.html'
    context_object_name = 'coins'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coins = list(Coin.objects.filter(user_id=self.request.user.profile.user_id))


        context.update({
            'coins': coins,


        })

        return context


class FiatWalletOverView(views.ListView):
    model = Deposit
    template_name = 'web/overview/fiat-overview.html'
    context_object_name = 'deposit'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deposits = list(Deposit.objects.filter(user_id=self.request.user.profile.user_id))
        is_owner = self.request.user.profile.user_id == self.request.user.id

        context.update({
            'deposits': deposits,
            'is_owner': is_owner,

        })

        return context


class CryptoWalletView(views.ListView):
    model = Coin
    template_name = 'web/generic/cryptowallet.html'
    context_object_name = 'coins'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coins = list(Coin.objects.filter(user_id=self.request.user.profile.user_id))
        is_owner = self.request.user.profile.user_id == self.request.user.id

        context.update({
            'coins': get_unique_object(coins),
            'is_owner': is_owner,

        })

        return context


class FiatWalletView(views.TemplateView):
    model = Deposit
    template_name = 'web/generic/fiatwallet.html'
    context_object_name = 'deposit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deposits = list(Deposit.objects.filter(user_id=self.request.user.profile.user_id))
        total_balance = sum([el.amount for el in deposits])
        currency = "".join([cur.currency for cur in deposits])
        is_owner = self.request.user.profile.user_id == self.request.user.id

        context.update({
            'deposits': deposits,
            'balance': total_balance,
            'is_owner': is_owner,
            'currency': currency,

        })

        return context
