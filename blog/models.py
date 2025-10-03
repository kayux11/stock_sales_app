from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField(default=0)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales")
    quantity_sold = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    date_sold = models.DateTimeField(auto_now_add=True)
    sold_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity_sold}"


class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class CashFlow(models.Model):
    total_sales = models.DecimalField(max_digits=14, decimal_places=2)
    total_expenses = models.DecimalField(max_digits=14, decimal_places=2)
    net_profit = models.DecimalField(max_digits=14, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CashFlow {self.date.date()}"
