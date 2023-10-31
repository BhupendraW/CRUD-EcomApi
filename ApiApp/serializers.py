from rest_framework import serializers
from .models import Company,Category,ECommerce


#create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Category
        fields="__all__"
        
        
        
class ECommerceSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()    
    class Meta:
        model=ECommerce
        fields="__all__"