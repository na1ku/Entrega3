Claro, aquí tienes el archivo README en español:

---

# Proyecto: Registro de Archivos

## Descripción

El proyecto Registro de Archivos es un script en Python diseñado para listar los nombres de los archivos dentro de un directorio especificado y guardar esta lista en un archivo de texto. El script solicita la entrada del usuario para el directorio a escanear y la ubicación del archivo de salida.

## Funcionalidades

- Lista todos los archivos en un directorio especificado.
- Guarda la lista de nombres de archivos en un archivo de texto especificado.
- Proporciona indicaciones amigables para el usuario.

## Requisitos

- Python 3.x

## Instalación

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/na1ku/Entrega3
   cd Entrega3
   ```

2. **Instalar Paquetes Requeridos:**

   Este proyecto no tiene dependencias externas. Solo utiliza el módulo incorporado `os`.

## Uso

1. **Ejecutar el Script:**

   Navega al directorio del proyecto y ejecuta el script de Python.

   ```bash
   python log_de_archivos.py
   ```

2. **Sigue las Indicaciones:**

   - Introduce la ruta al directorio que quieres escanear.
   - Introduce la ruta y el nombre del archivo de salida donde se guardará la lista de nombres de archivos (por ejemplo, `D:\\Desktop\\lista_de_archivos.txt`).

## Ejemplo

Después de ejecutar el script, verás una salida similar a la siguiente:

```plaintext
Enter the path to the directory: C:\Users\NombreDeUsuario\Documents
Enter the path and name of the output text file: C:\Users\NombreDeUsuario\Documents\lista_de_archivos.txt

List of files:
documento1.txt
imagen1.png
presentacion.pptx
...
```

El script creará un archivo de texto (`lista_de_archivos.txt`) que contiene la lista de nombres de archivos en el directorio especificado.

## Manejo de Errores

El script incluye manejo de errores para problemas comunes como errores de permisos y rutas de archivo inválidas. Asegúrate de proporcionar entradas válidas para evitar errores.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contribuir

Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request en GitHub.

## Contacto

Para cualquier pregunta o comentario, por favor contacta a Naiku en [njlamberti@gmail.com].

---
