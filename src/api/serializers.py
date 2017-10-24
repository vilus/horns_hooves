from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from page.models import Category, Good


class CategorySerializer(ModelSerializer):
    changed_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'changed_by')


class GoodSerializer(ModelSerializer):
    changed_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Good
        fields = ('id', 'name', 'description', 'in_stock', 'category', 'price', 'changed_by')
