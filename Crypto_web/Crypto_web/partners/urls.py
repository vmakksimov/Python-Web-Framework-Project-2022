from django.urls import path

from Crypto_web.partners.views import CreatePartnersView, PartnersView, PartnersDeleteView

urlpatterns = (
    path('create/', CreatePartnersView.as_view(), name='add partner'),
    path('all/', PartnersView.as_view(), name='partners'),
    path('delete/<int:pk>/', PartnersDeleteView.as_view(), name='delete partner'),
)
