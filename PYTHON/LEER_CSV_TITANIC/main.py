import csv 

# Sexo indice4
titanic = []
dic = {}
dic["problema1"] = {}
dic["problema1"]["vivos"] = 0
dic["problema1"]["murio"] = 0
dic["problema3"] = {}
dic["problema3"]["clases"] = []
dic["problema4"] = {}
dic["problema4"]["sexo"] = {'M':0,'F':0}

with open('titanic.csv') as archivo:
    datos = csv.reader(archivo,delimiter="\t")
    for linea in datos:
        titanic.append(linea)

titulos = titanic[0]
print(titulos)
del(titanic[0])

for pasajero in titanic:
    if pasajero[1] =="1":
        dic["problema1"]["vivos"] +=1
    elif pasajero[1]=="0":
        dic["problema1"]["murio"] +=1
    if pasajero[2] not in dic["problema3"]["clases"]:
        dic["problema3"]["clases"].append(pasajero[2])
    if pasajero[4]=='male':
        dic["problema4"]["sexo"]['M']+=1
    elif pasajero[4]=="female":
        dic["problema4"]["sexo"]['F']+=1
    
print("*"*10)
print("La cantidad de personas que sobrevivieron fueron : ",dic["problema1"]["vivos"])
porcentaje_sobrevivientes = (dic["problema1"]["vivos"] / (dic["problema1"]["vivos"]+dic["problema1"]["murio"]))*100
print("*"*10)
print("Sobrevivientes porcentaje = ",porcentaje_sobrevivientes,"%")
print("*"*10)
print("La cantidad de clases que hay = ",len(dic["problema3"]["clases"]))
print("*"*10)
print("La cantidad de hombres es de :",dic["problema4"]["sexo"]["M"])
print("La cantidad de mujeres es de :",dic["problema4"]["sexo"]["F"])