from django.db import models
from customers.models import Customer
from products.models import Product
# Create your models here.
class Order(models.Model):
	LIVE=1
	DELETE=0
	DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
	CART_STAGE=0
	ORDER_CONFIRMED=1
	ORDER_PROCESSED=2
	ORDER_REJECTED=4
	ORDER_DELIVERED=3
	id = models.AutoField(primary_key=True)
	owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
	elete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	STATUS_CHOICE=(
			(ORDER_PROCESSED,'ORDER_PROCESSED'),
			(ORDER_REJECTED,'ORDER_REJECTED'),
			(ORDER_DELIVERED,'ORDER_DELIVERED'),
			(ORDER_CONFIRMED,'ORDER_CONFIRMED')
		)
	order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)

	def __str__(self) -> str:
		return "order-{}-{}".format(self.id,self.owner.user.username)

class OrderedItem(models.Model):
	product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='added_carts')
	quantity=models.IntegerField(default=1)
	owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')
