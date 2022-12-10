from django.urls import path

from Crypto_web.event.views import CreateEventView, EventView, EventDetailView, EventEditView, EventDeleteView

urlpatterns = (
    path('', EventView.as_view(), name='events'),
    path('create/', CreateEventView.as_view(), name='create event'),
    path('details/<int:pk>/', EventDetailView.as_view(), name='event details'),
    path('edit/<int:pk>/', EventEditView.as_view(), name='update event'),
    path('delete/<int:pk>/', EventDeleteView.as_view(), name='delete event'),

)