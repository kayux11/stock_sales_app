from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(default=timezone.now)

    def clean(self):
        # Prevent negative stock sales
        if self.quantity > self.product.quantity:
            raise ValidationError(f"Not enough stock for {self.product.name}. Only {self.product.quantity} left.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Run validation before saving
        super().save(*args, **kwargs)
        # Reduce stock only after successful validation
        self.product.quantity -= self.quantity
        self.product.save()

    def __str__(self):
        return f"Sale of {self.quantity} {self.product.name}"


class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class CashFlow(models.Model):
    total_sales = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_expenses = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    net_cash_flow = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date = models.DateTimeField(default=timezone.now)

    def update_cash_flow(self):
        total_sales = sum(s.product.price * s.quantity for s in Sale.objects.all())
        total_expenses = sum(e.amount for e in Expense.objects.all())
        self.total_sales = total_sales
        self.total_expenses = total_expenses
        self.net_cash_flow = total_sales - total_expenses
        self.save()

    def __str__(self):
        return f"Cash Flow on {self.date.strftime('%Y-%m-%d')}"
