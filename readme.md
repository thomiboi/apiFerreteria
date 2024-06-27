# Grupo

- Thomas Rojas
- Sebastian Morales
- Nicolas Palma

# Pasos para Hacerlo Funcionar

1. **Eliminar el Entorno Virtual Existente:**

   - Elimina la carpeta `myvenv` existente para empezar con un entorno limpio.

2. **Crear un Nuevo Entorno Virtual:**

   - Dentro de la terminal, estando en la carpeta raíz del proyecto, ejecuta:
     ```sh
     python -m venv myvenv
     ```

3. **Activar el Entorno Virtual:**

   - Ejecuta el siguiente comando para activar el entorno virtual:
     ```sh
     ./myvenv/Scripts/activate
     ```

4. **Instalar las Dependencias:**

   - Con el entorno virtual activado, instala las dependencias del proyecto ejecutando:
     ```sh
     pip install -r requirements.txt
     ```

5. **Ejecutar el Servidor de Desarrollo:**

   - Inicia el servidor de desarrollo de Django con el siguiente comando:
     ```sh
     python manage.py runserver
     ```

6. **Probar la Aplicación:**
   - Ahora, la aplicación debería estar funcionando correctamente y lista para ser probada.

## URLs Importantes

- **[Index](http://127.0.0.1:8000/):** Página principal de la aplicación.
- **[Precios en Euros](http://127.0.0.1:8000/euro/):** Información sobre los precios en euros.
- **[Django REST Framework](http://127.0.0.1:8000/sistema/):** Interfaz del Django REST Framework.
- **[API de Productos](http://127.0.0.1:8000/sistema/indexproducto/):** Visualizar la lista de productos y formulario para agregar nuevos productos a la API.
- **[Panel de Administración](http://127.0.0.1:8000/admin/):** Acceso al panel de administración de Django.
- **[Documentación](http://127.0.0.1:8000/docs/):** Documentación interactiva generada automáticamente por Django.

# Para Ejecutar las Pruebas

Para ejecutar las pruebas unitarias, primero se debe inicializar la aplicación con los comandos anteriores. Una vez inicializada la aplicación, se pueden ejecutar las pruebas. Todas las pruebas unitarias se encuentran en el archivo `tests.py`.

## Ejecutar Todas las Pruebas

Para ejecutar todas las pruebas de una vez:

```sh
python manage.py test
```

### Scripts para las Pruebas Unitarias

#### Modelo Producto:

- **Probar la existencia del producto creado en SetUp:**
  ```sh
  python manage.py test sistema.tests.ProductoModelTest.test_producto_existencia
  ```
- **Probar que el campo nombre tenga longitud maxima de 100:**

```sh
 python manage.py test sistema.tests.ProductoModelTest.test_producto_nombre_max_length
```

#### Página Index:

- **Probar que la pagina index está funcionando:**

```sh
 python manage.py test sistema.tests.ProductoModelTest.test_index_page_status_code
```

- **Testear la funcionalidad de la barra de busqueda en index:**

```sh
python manage.py test sistema.tests.ProductoModelTest.test_index_page_search_bar
```

- **Testear que la pagina euro esta funcionando:**

```sh
python manage.py test sistema.tests.ProductoModelTest.test_euro_view
```

#### Pruebas de intgración

- **Probar la creación de un producto y convertir el precio en euro del producto a través de la API:**

```sh
python manage.py test sistema.tests.ProductoIntegrationTest.test_producto_creation_and_euro_price_integration
```

- **Probar la creación de un producto y validación de que existe en el listado:**

```sh
python manage.py test sistema.tests.ProductoListIntegrationTest.test_producto_creation_and_list
```

- **Probar la integración para la actualización de un producto:**

```sh
python manage.py test sistema.tests.ProductoUpdateIntegrationTest.test_producto_update

```

- **Probar la integración para la eliminación de un producto:**

```sh
python manage.py test sistema.tests.ProductoDeleteIntegrationTest.test_producto_delete
```

- **Prueba de integración para la búsqueda de objetos:**

```sh
python manage.py test sistema.tests.ProductoSearchIntegrationTest.test_producto_search

```
