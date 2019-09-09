from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pub, name='listar_pub'),
    path('pub/<int:pk>/', views.detalle_pub, name='detalle_pub'),
    path('pub/nuevo/', views.nuevo_pub, name='nuevo_pub'),

]