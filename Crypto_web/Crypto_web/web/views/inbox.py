from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views import generic as views

from Crypto_web.web.forms import DeleteMessageForm
from Crypto_web.web.models import ContactUs


class MessageView(views.DetailView):
    model = ContactUs
    template_name = 'web/inbox/message.html'
    context_object_name = 'message'
    paginate_by = 3

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message = list(ContactUs.objects.filter(author_id=self.object.author_id))
        total_messages = len(message)

        profiles = ContactUs.objects.all()

        paginator = Paginator(profiles, per_page=5)


        context.update({
            'messages': message,
            'total_messages': total_messages,
            'paginator': paginator.get_page(1),
        })

        return context


class MessageSentView(views.TemplateView):
    model = ContactUs
    template_name = 'web/inbox/message-sent.html'
    context_object_name = 'sent'

#
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MessageDeleteView(views.DeleteView):
    model = ContactUs
    form_class = DeleteMessageForm
    template_name = 'web/inbox/message-delete.html'
    success_url = reverse_lazy('dashboard')