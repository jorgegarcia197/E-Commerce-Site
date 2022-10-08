from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer


from .models import Product


# Create your views here.


# Function based views
@api_view(["GET"])
def get_routes(request):
    return Response("Hello World")


@api_view(["GET"])
def get_products(request):
    products = Product.objects.all()
    return Response(ProductSerializer(products, many=True).data)


@api_view(["GET"])
def get_product(request, pk):
    product = Product.objects.get(_id=pk)
    return Response(ProductSerializer(product, many=False).data)
