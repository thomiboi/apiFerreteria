from django.urls import path,include
from rest_framework import routers
from . import views
from .views import index,euro_view

router=routers.DefaultRouter()
router.register(r'producto',views.ProductoViewSet)
# path(ruta, funcion en views, nombre en html)

urlpatterns = [
    path('index/', views.index, name='index'),
    path('euro/', euro_view, name='euro_view'),
    path('',include(router.urls))
]