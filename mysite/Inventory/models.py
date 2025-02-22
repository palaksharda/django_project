from django.db import models

# Create your models here.
class Category(models.Model):
   name= models.CharField(max_length=100)
   description=models.TextField(blank=True, null=True)
   def __str__(self):
       return self.name
  


class Product(models.Model):
   name= models.CharField(max_length=100)
   description=models.TextField(blank=True, null=True)
   price=models.DecimalField(max_digits=10 , decimal_places=2)
   quantity=models.PositiveIntegerField()
   category=models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
   def __str__(self):
       return self.name