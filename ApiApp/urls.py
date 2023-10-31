from django.contrib import admin
from django.urls import path,include
from ApiApp.views import CompanyViewSet,ECommerceViewSet,CategoryViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'Category', CategoryViewSet)
router.register(r'ECommerce', ECommerceViewSet)

urlpatterns = [    
    path('',include(router.urls))
      
]


#companies/{companyId}/employees