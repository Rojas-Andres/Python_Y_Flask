import os 
import json 
from pprint import pprint
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="prueba_tecnica_1",
    port="5432"
)
connection.autocommit = True 

def crear_tabla_personas():
    cursor = connection.cursor()
    query = """create table IF NOT exists persona(id serial primary key, 
    nombre varchar(100),
    email varchar(100),
    identificacion varchar(100),
    sexo varchar(30),
    universidad_id integer,
    ciudad_id integer,
    CONSTRAINT fk_universidad FOREIGN KEY(universidad_id) REFERENCES universidad(id),
    CONSTRAINT fk_ciudad FOREIGN KEY(ciudad_id) REFERENCES ciudad(id)
    )"""
    cursor.execute(query) 

def crear_tabla_universidad():
    cursor = connection.cursor()
    query = """create table IF NOT exists universidad(id serial primary key , nombre varchar(100))"""
    cursor.execute(query)

def crear_tabla_ciudad():
    cursor = connection.cursor()
    query = """create table IF NOT exists ciudad(id serial primary key , nombre varchar(100))"""
    cursor.execute(query)   

def crear_tablas():
    crear_tabla_universidad() 
    crear_tabla_ciudad()
    crear_tabla_personas()

def insertar_universidad(universidad):
    
    cursor = connection.cursor()
    universidad = universidad.replace("'",'')
    query = f""" SELECT * from universidad where nombre='{universidad}' """
    cursor.execute(query)
    if cursor.fetchone() is None:
        query =f"""INSERT INTO universidad(nombre) values('{universidad}')"""
        cursor.execute(query)
    query = f""" SELECT * from universidad where nombre='{universidad}' """
    cursor.execute(query)
    id_universidad = cursor.fetchone()[0]
    cursor.close()
    return id_universidad

def insertar_ciudad(ciudad):
    cursor = connection.cursor()
    ciudad = ciudad.replace("'",'')
    query = f""" SELECT * from ciudad where nombre='{ciudad}' """
    cursor.execute(query)
    if cursor.fetchone() is None:
        query =f"""INSERT INTO ciudad(nombre) values('{ciudad}')"""
        cursor.execute(query)
    #Sacamos el id de la ciudad a la que vamos a hacer referencia en persona
    query = f""" SELECT * from ciudad where nombre='{ciudad}' """
    cursor.execute(query)
    id_ciudad = cursor.fetchone()[0]
    cursor.close() 
    return id_ciudad

def insertar_persona(universidad,ciudad,nombre,email,sexo,identificacion):
    cursor = connection.cursor()

    query = f""" INSERT INTO persona(nombre,email,identificacion,sexo,universidad_id,ciudad_id)
    values 
    ('{nombre}','{email}','{identificacion}','{sexo}',{universidad},{ciudad})
    """
    cursor.execute(query)
    cursor.close()


def leer_archivos():
    directorio = os.getcwd()
    with os.scandir(path=directorio) as itr:
        archivos_json = [i.name for i in itr if i.is_file() and i.name.split('.')[1]=='json' and 'informacion' in i.name.split('.')[0]]
        for i in archivos_json:
            f = open(i,encoding="utf8")
            data = json.load(f)
            for j in data:
                id_universidad = insertar_universidad(j["universidad"])
                id_ciudad = insertar_ciudad(j["ciudad"])
                insertar_persona(id_universidad,id_ciudad,j["nombre"],j["email"],j["sexo"],j["identificacion"])
            f.close()
            

if __name__ == "__main__":
    crear_tablas()
    leer_archivos()