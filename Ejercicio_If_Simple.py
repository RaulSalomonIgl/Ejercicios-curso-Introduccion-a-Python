'''Realizar un programa que solicite tu año de nacimiento y muestre en pantalla tu edad'''
##Declaracion de variable y asignación de valor
Año_Actual = 2020

##DEclaración de variable y solicitud de insercción de datos
Año_Nacimiento = int(input("Dame tu año de nacimiento:"))

Edad = 2020 - Año_Nacimiento

print("¿Ya cumpliste años?")
print("1.- Si")
print("2.- No")
Opcion = int(input(": "))

if Opcion == 1:
    print("Tu Edad es:",Edad)
else:
    print("Tu Edad es:",Edad-1)