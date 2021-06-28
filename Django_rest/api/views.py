from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import Item_Info
from .serializers import BaseItemSerializer, BasePriceSerializer

# GET 127.0.0.1:8000/api/hello/ 에 요청보내면 hello world print 하는 api임
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")


@api_view(['GET'])
def ItemAPI(request, id):
    this_item = Item_Info.objects.get(pid=id)
    serializer = BaseItemSerializer(this_item)
    return Response(serializer.data)
# => pid=id01에 대해 리턴된 Response: {'pid': id01, 'category_L': 0, 'name': 'can_pepsi', 'value': 5, 'price': 1500}


@api_view(['GET'])
def PriceAPI(request, id):
    this_price = Item_Info.objects.get(pid=id)
    serializer = BasePriceSerializer(this_price)
    return Response(serializer.data)
# => pid=id01에 대해 리턴된 Response: {'pid': id01,  'price': 1500}
