#  Sistema Gestor de Archivos en Python

Este es un programa interactivo escrito en Python que permite gestionar archivos y carpetas directamente desde la consola. Ideal para practicar manipulación de archivos con la biblioteca estándar (`os`, `shutil`, `mimetypes`).

---

## ⚙️ Funcionalidades

1. **Listar archivos** del directorio actual.
2. **Crear archivos** de texto o binarios.
3. **Eliminar archivos**.
4. **Renombrar archivos**.
5. **Crear carpetas**.
6. **Mover archivos** a otras carpetas.
7. **Copiar archivos** a otras carpetas.
8. **Eliminar carpetas vacías**.
9. **Salir del programa**.

---

##  Lógica del Programa

- El programa se ejecuta dentro de un bucle `while` mostrando un menú.
- Cada opción llama a una función personalizada que gestiona archivos usando los módulos `os`, `shutil`, y `mimetypes`.
- Se realizan controles de errores comunes como archivos no encontrados, errores de tipo, archivos duplicados, etc.

---

##  Dependencias

Este programa solo utiliza **módulos estándar de Python**, por lo que no es necesario instalar paquetes externos.

```python
import os
import mimetypes
import shutil
```

---

##  Validaciones y Características

- Verificación de tipos MIME para distinguir si un archivo es de texto o binario.
- Control de errores con `try/except`.
- Interfaz de consola amigable.
- Identificación automática del tipo de archivo durante la carga.

---

## Ejecución

```bash
python gestor_archivos.py
```

Luego, sigue las instrucciones del menú.

---

##  Mejoras Sugeridas

- Implementar interfaz gráfica (usando `tkinter` o `PyQt`).
- Soporte para editar archivos.
- Gestión de archivos recursiva (subcarpetas).
- Implementar un historial de acciones.

---

##  Autor

Desarrollado como parte de ejercicios prácticos de manipulación de archivos en Python.
