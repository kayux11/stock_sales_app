from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import Product, Sale, Expense, CashFlow
from .serializers import ProductSerializer, SaleSerializer, ExpenseSerializer, CashFlowSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('-date_sold')
    serializer_class = SaleSerializer

    def create(self, request, *args, **kwargs):
        """
        On sale creation:
         - verify product exists and sufficient quantity
         - compute total_price if not provided
         - decrement product.quantity
        """
        data = request.data.copy()
        product_id = data.get('product')
        if product_id is None:
            return Response({"detail": "product field is required."}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            product = get_object_or_404(Product, pk=product_id)
            try:
                qty = int(data.get('quantity_sold', 0))
            except (TypeError, ValueError):
                return Response({"detail": "quantity_sold must be an integer."}, status=status.HTTP_400_BAD_REQUEST)

            if qty <= 0:
                return Response({"detail": "quantity_sold must be greater than zero."}, status=status.HTTP_400_BAD_REQUEST)

            if product.quantity < qty:
                return Response({"detail": "Insufficient stock."}, status=status.HTTP_400_BAD_REQUEST)

            # if total_price not provided, compute from product.selling_price
            if not data.get('total_price'):
                data['total_price'] = str(product.selling_price * qty)

            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            # decrement product stock
            product.quantity -= qty
            product.save()

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('-date')
    serializer_class = ExpenseSerializer

class CashFlowViewSet(viewsets.ModelViewSet):
    queryset = CashFlow.objects.all().order_by('-date')
    serializer_class = CashFlowSerializer
