

# Create your views here.

from django.urls import reverse_lazy
from django.views import generic as views

from Crypto_web.helparticle.forms import CreateArticleForm, UpdateArticleForm, DeleteArticleForm
from Crypto_web.helparticle.models import HelpArticle




class CreateArticleView(views.CreateView):
    form_class = CreateArticleForm
    template_name = 'helparticles/create_article.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class HelpArticleView(views.ListView):
    model = HelpArticle
    template_name = 'news/news.html'
    context_object_name = 'articles'



class ArticleDetailView(views.DetailView):
    model = HelpArticle
    template_name = 'helparticles/details_article.html'
    context_object_name = 'article'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ArticleEditView(views.UpdateView):
    model = HelpArticle
    form_class = UpdateArticleForm
    template_name = 'helparticles/edit_article.html'
    context_object_name = 'article'
    success_url = reverse_lazy('index')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



class ArticleDeleteView(views.DeleteView):
    model = HelpArticle
    form_class = DeleteArticleForm
    template_name = 'helparticles/delete_article.html'
    success_url = reverse_lazy('dashboard')