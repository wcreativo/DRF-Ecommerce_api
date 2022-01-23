
from rest_framework import serializers
from apps.products.models import Product


class ProductSerializers(serializers.ModelSerializer):
    # StringRelatedField muestra el str del modelo relacionado
    # measure_unit = serializers.StringRelatedField()
    # category_product = serializers.StringRelatedField()

    class Meta:
        model = Product
        exclude = ('state', 'create_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
        # Se sobreescribe el metodo to_representation para mostrar los campos relacionados
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image if instance.image != '' else '',
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description
        }


