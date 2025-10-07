from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SaleViewSet, ExpenseViewSet, CashFlowViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'cashflows', CashFlowViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
