""" Module that defines the class FeedDb and Command to define a custom
django admin command to feed the database with categories and products
retrieved from Openfoodfacts API """

from django.core.management.base import BaseCommand, CommandError
from products.models import Product, Category
from products.get_data_from_openfoodfacts import GetDataFromOpenfoodfacts


class FeedDb:
    """ Class used to call get_data_from_openfoodfacts
    and feed the database """

    def __init__(self, nb_prod=None, nb_cat=None, categories=[]):
        self.nb_prod = nb_prod
        self.nb_cat = nb_cat
        self.categories = categories

    def add_data(self):
        data = GetDataFromOpenfoodfacts(
            nb_prod=self.nb_prod,
            nb_cat=self.nb_cat,
            categories=self.categories
        )
        data.get_products()
        for cat in data.cats:
            category, _ = Category.objects.get_or_create(name=cat)
            for product in data.cats[cat]["products"]:
                prod, _ = Product.objects.get_or_create(
                        name=product,
                        code=data.cats[cat]["products"][product][
                            "code"],
                        nutrition_grade=data.cats[cat]["products"][
                            product]["nutrition_grade"],
                        image=data.cats[cat]["products"][product][
                            "image_url"],
                        image_nutrition=data.cats[cat]["products"][
                            product]["image_nutrition_small_url"],
                        url=data.cats[cat]["products"][product]["url"]
                    )
                category.products.add(prod)

    def delete_data(self):
        Product.objects.all().delete()
        Category.objects.all().delete()


class Command(BaseCommand):
    """ Class used to defin the custom admin commands to feed or delete Categories
    and Products to the database """

    help = 'Feed the database with data fetched with Openfoodfacts API'

    def add_arguments(self, parser):
        parser.add_argument(
            '--nb_prod', '-np',
            type=int,
            dest='nb_prod',
            default=20,
            help='Number of product to add per categories'
        )
        parser.add_argument(
            '--nb_cat', '-nc',
            type=int,
            dest='nb_cat',
            default=20,
            help='Number of categories to add'
        )
        parser.add_argument(
            '--categories', '-c',
            action='append',
            dest='categories',
            help='List of categories to add'
        )
        parser.add_argument(
            '--delete_data', '-d',
            action='store_true',
            help='Delete products and categories from database'
        )

    def handle(self, *args, **kwargs):
        if kwargs['delete_data']:
            run = FeedDb()
            run.delete_data()
        else:
            run = FeedDb(
                kwargs['nb_prod'],
                kwargs['nb_cat'],
                kwargs['categories']                
            )
            run.add_data()
