from django.urls import path

from Crypto_web.helparticle.views import CreateArticleView, HelpArticleView, ArticleDetailView, ArticleEditView, \
        ArticleDeleteView

urlpatterns = (
        path('create-article', CreateArticleView.as_view(), name='create article'),
        path('articles/', HelpArticleView.as_view(), name='articles'),
        path('articles/details/<int:pk>/', ArticleDetailView.as_view(), name='article details'),
        path('articles/edit/<int:pk>/', ArticleEditView.as_view(), name='update article'),
        path('articles/delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete article'),
)