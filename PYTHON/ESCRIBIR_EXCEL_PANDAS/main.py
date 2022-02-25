import psycopg2
import pandas as pd 
connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="pruebas",
    port="5432"
)
query = """SELECT id,first_name,last_name, email from datos"""
df = pd.read_sql(query,con=connection)
print(df)
df.to_excel('datos.xlsx',index=False)