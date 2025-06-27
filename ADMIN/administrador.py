import os
import mimetypes
import shutil

def listar_archivos():
    for archivo in os.listdir():
        print(archivo)

def crear_achivos(nombre, archivo, es_binario = False):
    modo = 'wb' if es_binario else 'w'
    with open(nombre, modo) as f:
        f.write(contenido)
        print(f"Archivo {nombre} creado;")

def eliminar_archivos(nombre):
    try:
        os.remove(nombre)
        print(f"Archivo {nombre} eliminado.")
    except FileNotFoundError:
        print("No se encontro el archivo.")

    except OSError as e:
        print("Erro al eliminar el archivo: {e}")

def identificar_archivos(ruta):
    tipo, _= mimetypes.guess_type(ruta)
    if not tipo:
        print("No se reconoce el tipo de archivo")
        return None
    return tipo

def subir_archivo(ruta):
    tipoArchivo = identificar_archivos(ruta)
    if tipoArchivo:
        try:
            es_binario = not tipoArchivo.startswith('text')
            with open(ruta, 'rb' if es_binario else 'r') as f:
                contenido = f.read()
            nombre = os.path.basename(ruta)
            crear_achivos(nombre, contenido, es_binario)
        except Exception as e:
            print(f"Error al subir el archivo: {e}")
    else:
        print("Tipo de archivo no soportado")

def renombrar_archivo(nombre_actual, nuevo_nombre):
    try:
        #with open(nombre, 'rb') as f:
            os.rename(nombre_actual, nuevo_nombre)
            print(f"Archivo {nombre_actual} renombrado como: {nuevo_nombre}.")
    except FileExistsError :
        print(f": Ya existe el archivo: {nuevo_nombre}")
    except FileNotFoundError:
        print(f"No se encontro el archivo: {nombre_actual}")

def crear_carpeta(nombre):
    try:
        os.mkdir(nombre)
        print("Carpeta '{nombre}' creada")
    except FileExistsError:
        print("Carpeta '{nombre}' ya existe.")
    except OSError as e:
        print(f"Error al crear la carpeta {nombre}: {e}")

def mover_archivo(nombre_archivo, destino):
    try:
        shutil.move(nombre_archivo, destino)
        print(f"El '{nombre_archivo}' ha sido movido a '{destino}'")
    except FileNotFoundError:
        print(f"No se reconoce el archivo: {nombre_archivo}")
    except OSError as e:
        print(f"Error al mover el arhivo: {nombre_archivo}: {e}")

def copiar_Archivo(nombre_archivo, destino):
    try:
        shutil.copy(nombre_archivo, destino)
        print(f"archivo {nombre} copiado a {destino}")
    except FileNotFoundError:
        print(f"No se encontro el archivo: {nombre_archivo}")
    except OSError as e:
        print(f"Error al copiar el archivo {nombre}: {e}")

def eliminarCarpeta(nombre):
    try:
        os.rmdir(nombre)
        print(f"La carpeta '{nombre}' ha sido eliminada")
    except FileNotFoundError:
        print(f"No se encontro la carpeta {nombre}")
    except OSError as e:
        print(f"Error al eliminar la carpeta {nombre}: {e}")

def solicitarOpcion():
    try:
        return int(input("Ingrese una opcion: "))
    except ValueError:
        return -1
    
while True:
    print("\nSistema gestor de archivos")
    print("============================")
    print("1. Listar Archivos")
    print("2. Crear Archivos")
    print("3. Eliminar Archivos")
    print("4. Renombrar Archivos")
    print("5. Crear Carpeta")
    print("6. Mover archivo a una carpeta")
    print("7. Copiar un archivo")
    print("8. Eliminar Carpeta")
    print("9. Salir Carpeta")

    opcion = solicitarOpcion()

    if opcion == 1:
        listar_archivos()
        break

    elif opcion == 2:
        nombre   = input("Ingrese el nombre del archivo: ")
        contenido = input("Ingrese el contenido del archivo: ")
        crear_achivos(nombre, contenido)
        break

    elif opcion == 3:
        nombre = input("Ingrese el nombre del archivo: ")
        eliminar_archivos(nombre)
        break
        

    elif opcion == 4:
        nombre_actual = input("Ingrese el nombre del archivo que desea renombrar: ")
        nuevo_nombre = input("Ingrese el nuevo nobre del archivo: ")
        renombrar_archivo(nombre_actual, nuevo_nombre)
        break

    elif opcion == 5:
        nombre_carpeta = input("Ingrese el nombre de la carpeta que desea crear: ")
        crear_carpeta(nombre_carpeta)
        break
        
    elif opcion == 6:
        nombre = input("Ingrese el nombre del archivo que desea mover: ")
        destino = input("Igrese el nombre de la carpeta a la que desea mover: ")
        mover_archivo(nombre, destino)
        break

    elif opcion == 7:
        nombre = input("Ingrese el nombre del archivo que desea copiar: ")
        destino = input("Igrese el nombre de 1la carpeta a la que desea copiar: ")
        copiar_Archivo(nombre, destino)
        break

    elif opcion == 8:
        nombre = input("Ingrese el nombre de l acarpeta: ")
        eliminarCarpeta(nombre)
        break

    elif opcion == 9:
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion invalida")