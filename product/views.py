from .serializers import ProductListSerializer, ProductCreateSelializer
from .models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.pagination import PageNumberPagination


class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSelializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


class ProductUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'id'
