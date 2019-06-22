from django.db import models


class Product(models.Model):
    """ Class defining the product model """

    NUTRITION_GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    code = models.CharField(max_length=200, blank=False, unique=True)
    name = models.CharField(max_length=200)
    nutrition_grade = models.CharField(
        max_length=1,
        choices=NUTRITION_GRADE_CHOICES
        )
    image = models.URLField(max_length=500, null=True)
    image_nutrition = models.URLField(max_length=500, null=True)
    url = models.URLField(max_length=500, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["nutrition_grade"]
        verbose_name_plural = "products"


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
