from django import forms


class SearchForm(forms.Form):
    searched_product = forms.CharField()
