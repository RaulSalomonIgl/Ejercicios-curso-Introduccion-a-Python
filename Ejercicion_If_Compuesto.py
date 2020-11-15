'''
Crear un programa que solicite al usuario ingresar una cantidad monetaria en pesos mexicanos y 
almacenarla en una variable, acontinuacion se le presentara un menu de cambios donde debera elegir
entre las siguientes opciones:
1.- Dolares
2.- Euros
3.- Yenes
Segun la opción seleccionada se mostrará la converción del valor registrado en pesos a el valor
monetario seleccionado. Si se ingresa una opción diferente a las mostradas debera mostrar un mensaje
"El valor ingresado no es valido".

Dolar = $20MXN
Euro = $24MXN
Yen = $5MXN
'''
Pesos = int(input("Ingresar una cantidad monetaria en pesos mexicanos:"))
print("A que moneda deseas combertirlo ")
print("1.- Dolares")
print("2.- Euros")
print("3.- Yenes")

opcion = int(input("¿Dime que opcion quieres?:"))

if opcion == 1:
    Resultado = Pesos / 20
    print("Tus",Pesos,"MXN en Dolares son $",Resultado)

elif opcion == 2:
    Resultado = Pesos / 24
    print("Tus",Pesos,"MXN en Euros son",Resultado,"€")

elif opcion == 3:
    Resultado = Pesos * 5
    print("Tus",Pesos,"MXN en Yenes son",Resultado,"¥")
    
else:
    print("El valor ingresado no es valido")