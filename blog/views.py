from django.http import HttpResponse
from rest_framework import generics
from .models import Product, Sale, Expense
from .serializers import ProductSerializer, SaleSerializer, ExpenseSerializer

def home(request):
    return HttpResponse(
        "<h1>Welcome to Stock Sales Management System</h1>"
        "<p>Use /admin to manage products, sales, and cash flow.</p>"
    )

# API Views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SaleListCreateView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class CashFlowSummaryView(generics.ListAPIView):
    serializer_class = ExpenseSerializer  # temporary placeholder
    queryset = Expense.objects.none()
