from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, View
from django.core.paginator import Paginator
from .models import Product
from .forms import SearchForm


class ProductDetailView(DetailView):
    model = Product
    slug_field = 'code'
    slug_url_kwarg = 'code'
    template_name = 'product_detail.html'


class SearchProductView(View):

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['searched_product']
            # prod = Product.objects.filter(name__icontains=query).first()
            # substitued_prod = prod.get_substitutes()
            # paginator = Paginator(substitued_prod, 6)
            # page = request.GET.get('page')
            # substitued_products = paginator.get_page(page)
            # return render(request, 'products/product_searched.html', {
            #     'searched_product': prod,
            #     'substitued_products': substitued_products,
            #     })
            # return redirect('substitutes/', {
            #     'searched_product': prod,
            #     'substitued_products': substitued_prod,
            #     })
            return redirect('substitutes/', query)

    # def get(self, request):
    #     prod = Product.objects.filter(name__icontains=self.query).first()
    #     substitued_prod = prod.get_substitutes()
    #     paginator = Paginator(substitued_prod, 6)
    #     page = request.GET.get('page')
    #     substitued_products = paginator.get_page(page)
    #     return render(request, 'products/product_searched.html', {
    #         'searched_product': prod,
    #         'substitued_products': substitued_products,
    #         })


class SubstitutedProductsView(View):

    def get(self, request, *args, **kwargs):
        # prod = request.GET.get("searched_product")
        # substitued_prod = request.GET.get("substitued_products")
        # print(prod)
        # print(substitued_prod)
        print(request)
        prod = Product.objects.filter(name__icontains=query).first()
        substitued_prod = prod.get_substitutes()
        paginator = Paginator(substitued_prod, 6)
        page = request.GET.get('page')
        substitued_products = paginator.get_page(page)
        return render(request, 'products/product_searched.html', {
            'searched_product': prod,
            'substitued_products': substitued_products,
            })