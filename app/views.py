from rest_framework import viewsets, filters
from .models import Supplier
from .serializers import SupplierSerializer
from .permissions import IsActiveEmployee
from django.shortcuts import render


def home(request):
    return render(request, "app/home.html")


class SupplierViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели поставщика. Использует специальное разрешение
    для ограничения доступа только для активных сотрудников.
    """

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [filters.SearchFilter]
    search_fields = ["country"]
