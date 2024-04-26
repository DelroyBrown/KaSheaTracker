from django.db import models


# Model for Ingredients
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Stored in grams or ml for precision
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=255)


# Model for Materials (like containers, labels)
class Material(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()  # Number of items
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=255)



