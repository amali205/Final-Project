from django.contrib import admin
from . import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode


@admin.register(models.Collection)
class admincollection(admin.ModelAdmin):
    list_display = ['title']
    


@admin.register(models.CartItem)
class admincartitem(admin.ModelAdmin):
    list_display = ['product' , 'quantity' , 'cart' ]


@admin.register(models.Cart)
class admincart(admin.ModelAdmin):
    list_display = ['id' , 'created_at' ]




@admin.register(models.Product )
class adminproduct(admin.ModelAdmin):
    list_display = ['title' , 'price' , 'inventory' , 'collection' , 'last_update']
    list_editable = ['price' , 'inventory']    

@admin.register(models.Customer)
class admincustomer(admin.ModelAdmin):
    list_display = ['user__first_name' , 'user__last_name' , 'membership' , 'user__email' ]
    list_editable = ['membership']
    list_per_page = 10
    search_fields = ['user__first_name__istartswith' , 'user__last_name__istartswith' ]
    ordering = ['user__first_name' , 'user__last_name' ]


    @admin.display(ordering='orders_count')
    def orders_count(self , customer):
        url = ( 
            reverse('admin:Store_order_changelist') 
            + '?' 
            + urlencode({'customer__id': str(customer.id)}) 
        )
        return format_html('<a href="{}">{}</a>' , url , customer.orders_count)

    
@admin.register(models.Order)
class adminorder(admin.ModelAdmin):
    list_display = ['customer' , 'payment_status' , 'placed_at']
    list_editable = ['payment_status']
    
@admin.register(models.OrderItem)
class adminorderitem(admin.ModelAdmin):
    list_display = ['product' , 'unit_price' , 'quantity' , 'order_id']    
   

    