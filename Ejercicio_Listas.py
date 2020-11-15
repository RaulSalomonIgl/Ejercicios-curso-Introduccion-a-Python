lstDatos = []

Cant_Datos = int(input("Ingresa la cantidad de datos que deseas almacenar: "))
for datos in range(0,Cant_Datos):
    dato = input("Ingresa un dato: ")
    lstDatos.append(dato) 

print(lstDatos)