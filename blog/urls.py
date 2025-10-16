from django.urls import path
from .views import (
    home,
    ProductListCreateView,
    SaleListCreateView,
    ExpenseListCreateView,
    CashFlowSummaryView,
)

urlpatterns = [
    path('', home, name='home'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('sales/', SaleListCreateView.as_view(), name='sale-list-create'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('cashflow/', CashFlowSummaryView.as_view(), name='cashflow-summary'),
]
