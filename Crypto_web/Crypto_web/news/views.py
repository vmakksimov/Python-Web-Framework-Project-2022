
from django.urls import reverse_lazy

# Create your views here.
from django.views import generic as views

from Crypto_web.news.forms import CreateNewsForm, UpdateNewsForm, DeleteNewsForm
from Crypto_web.news.models import News


class AddNewsView(views.CreateView):
    form_class = CreateNewsForm
    template_name = 'news/news_create.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class NewsView(views.ListView):
    model = News
    template_name = 'news/news.html'
    context_object_name = 'news'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = list(News.objects.all())

        context.update({
            'news': news,

        })
        return context


class NewsDetailView(views.DetailView):
    model = News
    template_name = 'news/details_news.html'
    context_object_name = 'news'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NewsEditView(views.UpdateView):
    model = News
    form_class = UpdateNewsForm
    template_name = 'news/edit_news.html'
    context_object_name = 'news'
    success_url = reverse_lazy('index')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



class NewsDeleteView(views.DeleteView):
    model = News
    form_class = DeleteNewsForm
    template_name = 'news/delete_news.html'
    success_url = reverse_lazy('dashboard')
