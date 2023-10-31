from django.db import models

# Create your models here.

class Company(models.Model):
        company_name = models.CharField(max_length=50,null=False,blank=False)


        def __str__(self):
                return self.company_name



class Category(models.Model):
        category_name = models.CharField(max_length=50,null=False,blank=False)


        def __str__(self):
                return self.category_name






class ECommerce(models.Model):
        item_code = models.CharField(max_length=50,null=False,blank=False)
        item_name = models.CharField(max_length=50,null=False,blank=False)
        company_name = models.ForeignKey(Company,  on_delete=models.CASCADE,null=False,blank=False
        )
        category_name = models.ForeignKey(Category,  on_delete=models.CASCADE,null=False,blank=False
        ) 
        

        price = models.IntegerField()


        def __str__(self):
                return self.item_name

