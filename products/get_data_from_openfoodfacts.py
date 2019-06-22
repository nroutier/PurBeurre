""" Module that defines the class Off_api """

import requests


class GetDataFromOpenfoodfacts:
    """ Class used to get the data from Openfoodfacts API """

    def __init__(self, nb_prod=None, nb_cat=None, categories=None):
        self.cats = {}
        self.nb_cat = nb_cat
        self.nb_prod = nb_prod
        self.categories = categories

    def get_categories(self):

        """ Function that gets data from openfoodfact api
        and return a dictionnary of categories with products """
        if not self.categories:
            cat_url = "https://fr.openfoodfacts.org/categories.json"
            r = requests.get(cat_url)
            all_cat = r.json()

            for tag in all_cat["tags"]:
                if(
                    (self.nb_cat) and
                    (self.cats.__len__() >= self.nb_cat)
                ):
                    break
                if "Aliment" not in tag["name"]:
                    self.cats[tag["name"]] = {
                        "url": tag["url"],
                        "products": {}
                    }
        else:
            for cat in self.categories:
                self.cats[cat] = {"products": {}}

    def get_products(self):
        self.get_categories()
        for cat in self.cats:
            search_url = "https://fr.openfoodfacts.org/cgi/search.pl?"
            options = {
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": cat,
                "page_size": "100",
                "action": "process",
                "json": "1"}
            r = requests.get(search_url, params=options)
            prods = r.json()

            for prod in prods["products"]:
                if (
                    (self.nb_prod) and
                    (self.cats[cat]["products"].__len__() >= self.nb_prod)
                ):
                    break

                if self.check_product_data(prod):
                    self.cats[cat]["products"][prod["product_name"]] = {
                        "code": prod["code"],
                        "image_url": prod["image_url"],
                        "image_nutrition_small_url": prod[
                            "image_nutrition_small_url"],
                        "nutrition_grade": prod["nutrition_grades"].upper(),
                        "url": prod["url"]
                    }

    def check_product_data(self, product):
        fields = [
            "code",
            "product_name",
            "image_url",
            "image_nutrition_small_url",
            "nutrition_grades",
            "url"
        ]
        for field in fields:
            if field not in product or not product[field]:
                return False
        return True
