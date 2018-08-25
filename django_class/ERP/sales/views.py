# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from sales.models import Product

# Create your views here.
def fun(req):
	return HttpResponse(["user1","user2","user3"])
def fun1(req):
	return HttpResponse(["customer1","customer2","customer4"])
def get_products(req):
	products = Product.objects.all()
	names=[]
	for product in products:
		names.append(product.name)
	return HttpResponse(names)
	


