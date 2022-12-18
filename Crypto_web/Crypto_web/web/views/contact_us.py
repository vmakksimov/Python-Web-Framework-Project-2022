
from django.urls import reverse_lazy
from django.views import generic as views

from Crypto_web.web.forms import CreateContactForm


class CreateContactView(views.CreateView):

    form_class = CreateContactForm
    template_name = 'web/generic/contact.html'
    success_url = reverse_lazy('message sent')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


