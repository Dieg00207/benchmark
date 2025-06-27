#importaciones
from disk_benchmark import disk_performance
from memory_benchmark import memory_performance
from cpu_benchmark import cpu_performance
from pc_info import print_pc_info
from gpu_benchmark import gpu_performance

#menu
def main():
    print("selecciona una opcion a ejecutar:")
    print("1. Disco Duro")
    print("2. Memoria RAM")
    print("3. Procesador")
    print("4. Tarjeta Grafica")
    print("5. Informacion del Sistema")

    choice = input(">")

    if choice == "1":
        disk_performance()

    elif choice == "2":
        memory_performance()
    
    elif choice == "3":
        cpu_performance()
    
    elif choice == "4":
        gpu_performance()

    elif choice == "5":
        print_pc_info()

    else: 
        print("Opcion no valida. ")

if _name=="main_":
    main()