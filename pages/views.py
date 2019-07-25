from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from products.forms import SearchForm
from products.models import Product
from products.views import ProductDetailView


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        form = SearchForm()
        context = super().get_context_data(*args, **kwargs)
        context['form'] = form
        return context


# def home(request):
#     # if request.method == 'POST':
#     #     form = SearchForm(request.POST)
#     #     if form.is_valid():
#     #         query = form.cleaned_data['searched_product']
#     #         prod = Product.objects.filter(name=query).first()
#     #         subtitued_prod = prod.get_substitutes()
#     #         # return render(request, 'products/product_detail.html', prod.code)
#     #         # return redirect('products/' + prod.code)
#     #         return redirect(prod.get_absolute_url())
#     #         # return redirect('ProductDetailView', code=prod.code)

#     # else:
#     #     form = SearchForm()
#     # return render(request, 'index.html', {'form': form})
#     form = SearchForm()
#     return render(request, 'index.html', {'form': form})


class LegalPageView(TemplateView):
    template_name = 'legal.html'
