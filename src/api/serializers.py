from rest_framework.serializers import ModelSerializer
from page.models import Category, Good


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class GoodSerializer(ModelSerializer):
    class Meta:
        model = Good
        fields = ('id', 'name', 'description', 'in_stock', 'category', 'price')
