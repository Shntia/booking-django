from django.urls import path, include


urlpatterns = [
    path('', include('reservations.api.urls')),
]

