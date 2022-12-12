
from django.contrib.auth import views as auth_views, logout, login

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from Crypto_web.accounts.forms import ProfileForms, DeleteForm, EditProfileForm
from Crypto_web.accounts.models import Profile
from Crypto_web.common.helpers import calculate_total_balance
from Crypto_web.services.ses import SESService
from Crypto_web.accounts.tasks import send_email_to_new_user

from Crypto_web.web.models import Coin, Deposit


# Create your views here.
class UserRegisterView(views.CreateView):
    form_class = ProfileForms
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        # sending email for registration to the user asynchronous
        send_email_to_new_user.delay(request.POST['email'])
        # sending email for registration to the user synchronous
        #SESService().send_email(request.POST['email'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login-view.html'

    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('index')


class UserLogOutView(views.View):
    def get(self, request):
        logout(request)
        return redirect('index')


class ProfileView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coins = list(Coin.objects.filter(user_id=self.object.user_id))
        fiat_balance = sum(el.amount for el in Deposit.objects.filter(user_id=self.object.user_id))
        crypto_balance = calculate_total_balance(coins)


        context.update({
            'total_coins': len(coins),
            'fiat_balance': fiat_balance,
            'crypto_balance': crypto_balance,
            'total_balance': fiat_balance + crypto_balance,
        })

        return context



def delete_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    total_balance = calculate_total_balance(list(Coin.objects.filter(user_id=request.user.id)))
    if total_balance > 0:
        return redirect('balance')

    if request.method == 'POST':
        form = DeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            logout(request)
            return redirect('index')
    else:
        form = DeleteForm(request.POST, instance=profile)

    context = {
        'form': form
    }

    return render(request, 'accounts/delete-profile.html', context)


class BalanceAvailableView(views.TemplateView):
    template_name = 'accounts/deletion-message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_context'] = True
        return context


class EditProfileView(views.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('index')
    context_object_name = 'profile'


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs








