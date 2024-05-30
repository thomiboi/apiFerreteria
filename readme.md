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
- **[Documentación](http://127.0.0.1:8000/docs/):** Documentación generada automáticamente por Django.
