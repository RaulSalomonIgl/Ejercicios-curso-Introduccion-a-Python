##Declaracion de variables y solicitud de insercción de datos
Numero1 = int(input("Ingresa un numero entero: "))
Numero2 = int(input("Ingresa un segundo numero entero: "))

##Se evalua la condición numero2 es MENOR que numero 1,
##mientras sea cierto se ejecutara el siguiente Código.
while Numero2 <= Numero1:
    Numero2 = int(input("Ingresa un nuevo numero entero: "))

print(Numero1)
print(Numero2)