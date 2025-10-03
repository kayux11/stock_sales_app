from django.contrib import admin
from .models import Product, Sale, Expense, CashFlow

admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Expense)
admin.site.register(CashFlow)
