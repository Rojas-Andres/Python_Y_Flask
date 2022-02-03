import os 

nuevo_carpeta = input("Nombre de la nueva carpeta: ")
directorio_actual = os.getcwd()
print("Este es su directorio",directorio_actual)
path = os.path.join(directorio_actual,nuevo_carpeta)
os.mkdir(path)