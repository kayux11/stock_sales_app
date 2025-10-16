from rest_framework import serializers
from .models import Product, Sale, Expense, CashFlow

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class CashFlowSerializer(serializers.ModelSerializer):
    net_cash_flow = serializers.ReadOnlyField()

    class Meta:
        model = CashFlow
        fields = ['id', 'date', 'total_sales', 'total_expenses', 'net_cash_flow']
