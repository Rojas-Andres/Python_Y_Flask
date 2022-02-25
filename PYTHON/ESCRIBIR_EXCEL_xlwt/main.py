import psycopg2
from xlwt import Workbook
connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="pruebas",
    port="5432"
)

connection.autocommit = True 

cursor = connection.cursor()
query = """ SELECT id,first_name,last_name,email from datos; """
cursor.execute(query)
rs = cursor.fetchall()
cursor.close()

wb = Workbook()
sheet = wb.add_sheet('Sheet 1')
sheet.write(0,0,'id')
sheet.write(0,1,'first_name')
sheet.write(0,2,'last_name')
sheet.write(0,3,'email')
contador = 1
for r in rs:
    sheet.write(contador,0,r[0])
    sheet.write(contador,1,r[1])
    sheet.write(contador,2,r[2])
    sheet.write(contador,3,r[3])
    contador+=1
wb.save('datos.xls')