import timeit
import platform
import psutil
import wmi

def print_pc_info():
    c = wmi.WMI()
    print("Información del Sistema:")

    # Procesador
    for cpu in c.Win32_Processor():
        print(f"CPU: {cpu.Name}, {cpu.NumberOfCores} núcleos")
    
    # Tarjeta Gráfica
    for gpu in c.Win32_VideoController():
        print(f"GPU: {gpu.Name}")

    # Memoria RAM
    ram = psutil.virtual_memory()
    print(f"Memoria RAM: {ram.total / (1024 ** 3):.2f} GB")

    # Almacenamiento
    for disk in c.Win32_DiskDrive():
        print(f"Disco de Almacenamiento: {disk.Model}, {int(disk.Size) / (1024 ** 3):.2f} GB")

if _name_ == "_main_":
    print_pc_info()

    #informacion del sistema
    print("Infromacion del sistema")
    print(f"Sistema operativo: {platform.system()}, {platform.release()}")
    print(f"Nombre del PC: {platform.node()}")
    print(f"Arquitectura: {platform.machine()}")
    print(f"Procesador: {platform.processor()}")