import os 

eliminar_carpeta = input("Nombre de la carpeta a eliminar : ")
directorio_actual = os.getcwd()

path = os.path.join(directorio_actual,eliminar_carpeta)

if os.path.exists(path):
    os.rmdir(path)
    print("La carpeta ha sido eliminada exitosamente")
else:
    print("La carpeta no existe ")