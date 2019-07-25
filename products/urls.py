from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('<slug:code>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('searched-substitutes', views.SearchProductView.as_view(), name='searched_substitutes'),
    path('substitutes', views.SubstitutedProductsView.as_view(), name='substitutes'),
]
