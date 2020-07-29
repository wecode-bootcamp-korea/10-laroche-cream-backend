from django.urls import path

from .views import MainView, AllItemView, DetailItemView

urlpatterns = [
    path('',MainView.as_view()),
    path('/allitem',AllItemView.as_view()),
    path('/detail',DetailItemView.as_view())
]
