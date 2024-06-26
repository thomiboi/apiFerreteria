from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
import requests
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Producto
from django.test import TestCase


####### Pruebas del modelo y visualizaciones de index/euro ########
class ProductoModelTest(TestCase):

    def setUp(self):
        "Probamos la creacion de un elemento en producto"
        self.producto = Producto.objects.create(
            nombre='PruebaUnitaria',
            precio= 15000,
            stock='20 unidades'
        )

    def test_producto_existencia(self):

        
        """Prueba la existencia del producto creado anteriormente"""
        producto = Producto.objects.get(nombre='PruebaUnitaria')
        self.assertEqual(producto.nombre, 'PruebaUnitaria')
        self.assertEqual(producto.precio, 15000)
        self.assertEqual(producto.stock, '20 unidades')

    def test_producto_nombre_max_length(self):
        """Prueba que el campo 'nombre' tenga una longitud máxima"""
        max_length = self.producto._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 100)


    def test_index_page_status_code(self):
        """prueba que la pagina de  index este funcionando correctamente"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_page_search_bar(self):
        """Testear la funcionalidad de la barra de busqueda en index"""
        search_term = 'Martillo'
        response = self.client.get(reverse('index'), {'search': search_term})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, search_term)

    def test_euro_view(self):
        """Probar la vista de euro"""
        response = self.client.get(reverse('euro'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Euro")
    


######### Pruebas de integracion ############
class ProductoIntegrationTest(APITestCase):

    def setUp(self):
        # Crear un producto que se usará en las pruebas
        self.producto = Producto.objects.create(
            nombre='PruebaIntegracion',
            precio=15000,
            stock='20 unidades'
        )
        # URL de la API del producto
        self.producto_url = reverse('producto-detail', kwargs={'pk': self.producto.pk})

    def test_producto_creation_and_euro_price_integration(self):
        """Prueba de integración para creación de producto y verificación de la API del valor del euro"""
        
        # Verificar la creación del producto
        response = self.client.get(self.producto_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'PruebaIntegracion')
        self.assertEqual(response.data['precio'], 15000)
        self.assertEqual(response.data['stock'], '20 unidades')

        # Verificar la API del valor del euro
        euro_api_url = 'https://mindicador.cl/api/euro'
        response = requests.get(euro_api_url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        
        # Validar que la API contiene la clave 'serie'
        self.assertIn('serie', data)
        
        # Validar que la serie no esté vacía y que contenga al menos un valor
        self.assertTrue(len(data['serie']) > 0)

        # Obtener el valor más reciente del euro
        euro_rate = data['serie'][0]['valor']
        self.assertIsInstance(euro_rate, (float, int))

        # Integrar la información del producto con la API del valor del euro
        precio_en_euros = self.producto.precio / euro_rate
        print(f"Precio del producto en euros: {precio_en_euros}")

        # Asegurar que el precio en euros es un valor positivo
        self.assertGreater(precio_en_euros, 0)

    
class ProductoListIntegrationTest(APITestCase):

    def test_producto_creation_and_list(self):
        """Prueba de integración para la creación de producto y validación de listado"""
        
        # Crear un producto
        producto_data = {
            'nombre': 'ProductoListado',
            'precio': 20000,
            'stock': '15 unidades'
        }
        response = self.client.post(reverse('producto-list'), producto_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verificar que el producto aparece en el listado
        response = self.client.get(reverse('producto-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(prod['nombre'] == 'ProductoListado' for prod in response.data))


class ProductoUpdateIntegrationTest(APITestCase):

    def setUp(self):
        self.producto = Producto.objects.create(
            nombre='ProductoOriginal',
            precio=10000,
            stock='10 unidades'
        )
        self.producto_url = reverse('producto-detail', kwargs={'pk': self.producto.pk})

    def test_producto_update(self):
        """Prueba de integración para la actualización de un producto"""
        
        # Actualizar el producto
        updated_data = {
            'nombre': 'ProductoActualizado',
            'precio': 12000,
            'stock': '5 unidades'
        }
        response = self.client.put(self.producto_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verificar que el producto se actualizó correctamente
        response = self.client.get(self.producto_url)
        self.assertEqual(response.data['nombre'], 'ProductoActualizado')
        self.assertEqual(response.data['precio'], 12000)
        self.assertEqual(response.data['stock'], '5 unidades')

class ProductoDeleteIntegrationTest(APITestCase):

    def setUp(self):
        self.producto = Producto.objects.create(
            nombre='ProductoEliminar',
            precio=10000,
            stock='10 unidades'
        )
        self.producto_url = reverse('producto-detail', kwargs={'pk': self.producto.pk})

    def test_producto_delete(self):
        """Prueba de integración para la eliminación de un producto"""
        
        # Eliminar el producto
        response = self.client.delete(self.producto_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verificar que el producto ya no está en el listado
        response = self.client.get(reverse('producto-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(any(prod['nombre'] == 'ProductoEliminar' for prod in response.data))


class ProductoSearchIntegrationTest(APITestCase):

    def setUp(self):
        Producto.objects.create(nombre='ProductoBuscar', precio=15000, stock='10 unidades')
        Producto.objects.create(nombre='ProductoBuscarDos', precio=20000, stock='5 unidades')

    def test_producto_search(self):
        """Prueba de integración para la búsqueda de productos"""
        
        # Buscar productos que contienen 'Buscar' en el nombre
        response = self.client.get(reverse('producto-list'), {'search': 'Buscar'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all('Buscar' in prod['nombre'] for prod in response.data))