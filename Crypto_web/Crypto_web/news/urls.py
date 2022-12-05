from django.urls import path

from Crypto_web.news.views import NewsView, AddNewsView, NewsDetailView, NewsEditView, NewsDeleteView

urlpatterns = (
    path('', NewsView.as_view(), name='news'),
    path('create/', AddNewsView.as_view(), name='create news'),
    path('details/<int:pk>/', NewsDetailView.as_view(), name='details news'),
    path('update/<int:pk>/', NewsEditView.as_view(), name='update news'),
    path('delete/<int:pk>/', NewsDeleteView.as_view(), name='delete news'),
)