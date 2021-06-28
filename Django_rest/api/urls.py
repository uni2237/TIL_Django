from django.urls import path, include
from .views import HelloAPI, ItemAPI, PriceAPI

urlpatterns = [
    path("hello/", HelloAPI),
    path("info/<str:id>", ItemAPI, name="get_item_info"),
    path("price/<str:id>", PriceAPI, name="get_item_price"),
]