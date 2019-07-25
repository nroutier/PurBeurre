from django.db import models
from django.urls import reverse


class Product(models.Model):
    """ Class defining the product model """

    code = models.CharField(max_length=200, blank=False, unique=True)
    name = models.CharField(max_length=200)
    nutrition_grade = models.CharField(max_length=1)
    image = models.URLField(max_length=500, null=True)
    image_nutrition = models.URLField(max_length=500, null=True)
    url = models.URLField(max_length=500, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["nutrition_grade"]
        verbose_name_plural = "products"

    def get_substitutes(self):
        grades = ["A", "B", "C", "D", "E"]
        id_product = grades.index(self.nutrition_grade)
        substitutes_grades = grades[:id_product]
        return Product.objects.filter(
            nutrition_grade__in=substitutes_grades,
            categories=self.categories.first()
        ).order_by('nutrition_grade')

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.code])


class Category(models.Model):
    """ Class defining the Category model """

    name = models.CharField(max_length=200)
    products = models.ManyToManyField(
        "Product",
        related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"
