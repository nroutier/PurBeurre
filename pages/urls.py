from django.urls import path

from .views import HomePageView, LegalPageView
# from .views import LegalPageView, home

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('', home, name='home'),
    path('legal/', LegalPageView.as_view(), name='legal')
]