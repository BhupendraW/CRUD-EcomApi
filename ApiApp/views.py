from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import Company,Category,ECommerce
from .serializers import CompanySerializer,ECommerceSerializer,CategorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class ECommerceViewSet(viewsets.ModelViewSet):
    queryset= ECommerce.objects.all()
    serializer_class=ECommerceSerializer
    
    #companies/{companyId}/emplyees
    @action(detail=True,methods=['get'])
    def ecommerce(self,request,pk=None):   
        try:                
            company=Company.objects.get(pk=pk)
            category = Category.objects.get(pk=pk)
            ecom=ECommerce.objects.filter(company_name=company,category_name=category)
            ecom_serializer=ECommerceSerializer(ecom,many=True,context={'request':request})
            return Response(ecom_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Item  might not exists !! Error'
            })


class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

