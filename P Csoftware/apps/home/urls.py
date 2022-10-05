from django.urls import path
from .views import *

urlpatterns = [
    path('index/', indexview.as_view(),name='index' ),
    path('clientes/', clientesview.as_view(),name='clientes' ),
    path('base/', baseview.as_view(),name='base' ),
    path('articulos/', articulosview.as_view(),name='articulos' ),
    path('pedidos/', pedidosview.as_view(),name='pedidos' ),
    path('login/', loginview.as_view(),name='login' ),
   
    
   
]
