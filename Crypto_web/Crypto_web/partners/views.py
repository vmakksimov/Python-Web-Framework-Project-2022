from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from Crypto_web.partners.forms import CreatePartnersForm


class CreatePartnersView(views.CreateView):
    form_class = CreatePartnersForm
    template_name = 'partners/create_partners.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs