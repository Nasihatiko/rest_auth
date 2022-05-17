from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('author', )

    def to_representation(self, instance):
        representation  = super().to_representation(instance)
        representation['author'] = instance.author.email
        return representation