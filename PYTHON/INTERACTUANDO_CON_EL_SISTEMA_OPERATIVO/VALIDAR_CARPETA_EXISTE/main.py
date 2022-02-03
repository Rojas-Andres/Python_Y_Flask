import os 

nuevo_carpeta = input("Nombre de la nueva carpeta: ")
directorio_actual = os.getcwd()

path = os.path.join(directorio_actual,nuevo_carpeta)

if os.path.exists(path):
    print("La carpeta ya existe")
else:
    os.mkdir(path)
    print("Carpeta creada")