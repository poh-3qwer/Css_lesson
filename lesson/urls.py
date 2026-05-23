from django.urls import path
from lesson import views


urlpatterns = [
    path("", views.rewiev_list, name='rewiev_list'),
]