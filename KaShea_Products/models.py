from django.db import models
from KaShea_Inventory.models import Ingredient


# Model for Products (e.g., types of cosmetics like Zen Butter)
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    # Relationship to ingredients
    ingredients = models.ManyToManyField(Ingredient, through="ProductIngredient")


# Through model to link products and ingredients with additional data
class ProductIngredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_required = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Quantity of each ingredient per unit product
