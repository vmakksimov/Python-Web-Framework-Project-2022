from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from Crypto_web.event.forms import CreateEventForm, UpdateEventForm, DeleteEventForm
from Crypto_web.event.models import CryptoEvent


# Create your views here.
class CreateEventView(views.CreateView):
    form_class = CreateEventForm
    template_name = 'events/create_event.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EventView(views.ListView):
    model = CryptoEvent
    template_name = 'events/events.html'
    context_object_name = 'events'



class EventDetailView(views.DetailView):
    model = CryptoEvent
    template_name = 'events/details_article.html'
    context_object_name = 'event'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EventEditView(views.UpdateView):
    model = CryptoEvent
    form_class = UpdateEventForm
    template_name = 'events/edit_article.html'
    context_object_name = 'event'
    success_url = reverse_lazy('index')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EventDeleteView(views.DeleteView):
    model = CryptoEvent
    form_class = DeleteEventForm
    template_name = 'events/delete_article.html'
    success_url = reverse_lazy('dashboard')