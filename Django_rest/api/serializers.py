
from rest_framework import serializers
from .models import Item_Info


class BaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Info
        fields = ('pid', 'category_L', 'name', 'value','price')

 
class BasePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Info
        fields = ('pid','price')

