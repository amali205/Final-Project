from django.db import models
import uuid
from django.conf import settings



class Collection(models.Model):
    title =models.CharField(max_length=20)
    def __str__(self):
        return self.title

class Product (models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    price = models.DecimalField(decimal_places=2 , max_digits= 6 )
    inventory = models.IntegerField()
    collection = models.ForeignKey(Collection , on_delete= models.PROTECT , related_name='products')
    last_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField()                     # for SEOcls
    
    def __str__(self):
        return self.title




class Customer(models.Model):
    membership_B='B'
    membership_s='S'
    membership_g='G'
    membership_c=[
        (membership_B , 'Bronze'),
        (membership_s,'Silver'),
        (membership_g,'Gold'),
    ]
   
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=30 , choices=membership_c , default=membership_B)
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE )       


    def __str__(self):
            return f'{self.user.first_name} {self.user.last_name}'




class Order(models.Model):
    p = 'pending'
    c = 'complete'
    f = 'failed'
  
    payment_c = [
        (p , 'pending'),
        (c , 'complete'),
        (f , 'failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status= models.CharField(max_length=30 , choices= payment_c , default=p)    
    customer =models.ForeignKey(Customer , on_delete=models.PROTECT)

    
    class Meta:
        permissions = [
            ('cancel_order' , 'can cancel order')
        ]



class OrderItem(models.Model):
    unit_price = models.DecimalField(max_digits=5 , decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    product = models.ForeignKey(Product , on_delete=models.PROTECT)
    order = models.ForeignKey(Order , on_delete=models.PROTECT , related_name='items')

    def __str__(self):
        return self.product.title 



class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()



    class Meta:
        unique_together = [['cart', 'product']]


    def __str__(self):
        return self.product.title




   