from curses import meta
from rest_framework import serializers
from apps.products.models import MeasureUnit, CategoryProduct, Product, Indicator

class MeasureUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureUnit
        exclude = ('state', 'create_date', 'modified_date', 'deleted_date')

class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        exclude = ('state', 'create_date', 'modified_date', 'deleted_date')

class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        exclude = ('state', 'create_date', 'modified_date', 'deleted_date')
    