from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
	featured_products=Product.objects.order_by('priority')[:3]
	latest_products=Product.objects.order_by('-id')[:3]
	context={'featured_products':featured_products,'latest_products':latest_products}
	return render(request,'index.html',context)
def list_products(request):
	"""_summary_
	returns product list page
	Args:
		request (_type_): _description_

	Returns:action="/order/add_to_cart"
		_type_: _description_
	"""
	page=request.GET.get('page',1)
	product_list=Product.objects.order_by('priority')
	product_paginator=Paginator(product_list,2)
	product_list=product_paginator.get_page(page)
	context={'products':product_list}
	return render(request,'products_layout.html',context)
def detailed_product(request,pk):
	product=Product.objects.get(pk=pk)
	context={'product':product}
	return render(request,'products_detail.html',context)

