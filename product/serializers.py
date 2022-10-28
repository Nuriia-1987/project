from rest_framework import serializers
from .models import Product
from rest_framework.exceptions import ValidationError


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSelializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=100)
    price = serializers.FloatField()
    about = serializers.CharField(min_length=10, max_length=1000)
    image = serializers.ImageField()
    is_active = serializers.BooleanField(default=True)

    def validate_product(self, product):
        try:
            Product.objects.get(id=product)
        except Product.DoesNotExist:
            raise ValidationError('Product Not Fount')
        return product
