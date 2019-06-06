from django.urls import path

from .views import HomePageView, LegalPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('legal/', LegalPageView.as_view(), name='legal'),
]