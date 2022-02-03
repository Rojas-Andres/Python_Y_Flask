import os

directorio = os.getcwd()
with os.scandir(path=directorio) as itr:
    for i in itr:
        if i.is_file():
            print("Es un archivo -> " ,i.name)
        elif i.is_dir():
            print("Es una carpeta -> ",i.name)