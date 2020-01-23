from django.urls import path
from references import views

urlpatterns = [
    path('spell', views.SpellAPIView.as_view())
]
