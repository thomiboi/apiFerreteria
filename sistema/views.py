from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProductoSerializer
from .models import Producto

import requests

# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def index(request):
    productos = Producto.objects.all()
    ciudad = 'Santiago,CL'
    valor_euro, fecha_actualizacion = obtener_valor_euro()
    temperatura, descripcion_clima, humedad = obtener_clima(ciudad)
    
    return render(request, "index.html", {
        'temperatura': temperatura,
        'descripcion_clima': descripcion_clima,
        'humedad': humedad,
        'productos': productos,
        'valor_euro': valor_euro,
        'fecha_actualizacion': fecha_actualizacion
    })

def obtener_clima(ciudad):
    clave_api = 'bc88622f74361d69d8329c887d6abb54'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={clave_api}&units=metric'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si hay un error al hacer la solicitud
        datos_clima = response.json()
        temperatura = datos_clima['main']['temp']
        descripcion_clima = datos_clima['weather'][0]['description']
        humedad = datos_clima['main']['humidity']
        return temperatura, descripcion_clima, humedad
    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud a la API:", e)
        return None, None, None

def euro_view(request):
    return render(request, 'euro.html')

def index_producto(request):
    api_url = "http://127.0.0.1:8000/sistema/indexproducto/?format=json"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        productos = response.json()
    else:
        productos = []

    context = {
        'productos': productos
    }
    
    return render(request, 'index.html', context)

def obtener_valor_euro():
    # URL de la API para obtener el valor del euro
    url = 'https://mindicador.cl/api/euro'
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()  # Parsear la respuesta JSON
        # Extraer la fecha y el valor más reciente del euro
        valor_euro = data['serie'][0]['valor']
        fecha_actualizacion = data['serie'][0]['fecha']
    else:
        valor_euro = None
        fecha_actualizacion = None

    # Devolver el valor del euro y la fecha de actualización
    return valor_euro, fecha_actualizacion