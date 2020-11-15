'''
Realizar un programa donde se muestre en un menu con las siguientes opciones:
1.- Calculadora.
2.- Tablas de Multiplicar.
3.- Calculadora de Edad.
4.- Crea un Usuario.
5.- Salir
'''

Menu = 0
while True:
    print("         MENU            ")
    print("1.- Calculadora")
    print("2.- Tablas de Multiplicar")
    print("3.- Calculadora de Edad")
    print("4.- Crear un Usuario")
    print("5.- Salir")
    Menu = int(input("Selección: "))
    if Menu == 1:
        ##Calculadora
        print("SUBMENU DE ACCIONES")
        print("1.-Sumar")
        print("2.-Restar")
        print("3.-Multiplicar")
        print("4.-Dividir")
        Opcion = int(input("Selecciona una opción: "))

        print("")
        print("Dame los dos valores")
        print("")

        valor1 = int(input("Dame el primer valor:"))
        valor2 = int(input("Dame el segundo valor:"))

        if Opcion == 1:
            resultado = valor1 + valor2
            print("La Suma de los dos valores es: ",resultado)

        elif Opcion ==2:
            resultado = valor1 - valor2
            print("La Resta de los dos valores es: ",resultado)

        elif Opcion == 3:
            resultado = valor1 * valor2
            print("La multiplicacion de los valores es: ",resultado)

        elif Opcion == 4:
            resultado = valor1 / valor2
            print("La divicion de los dos valores es: ",resultado)

        else:
            print("Tu opcion es incorrecta")

    elif Menu == 2:
        ##Tablas de Multiplicar
        Numero = int(input("Ingresa un numero: "))
        Limite = int(input("Limite de la tabla de multiplicaciones: "))

        for posicion in range(0,Limite):
            print(Numero,"X",posicion+1,"=",Numero*(posicion+1))

    elif Menu == 3:
        ##Calculadora de Edad
        Año_Actual = 2020
        Año_Nacimiento = int(input("Dame tu año de nacimiento:"))

        Edad = 2020 - Año_Nacimiento

        print("¿Ya cumpliste años?")
        print("1.- Si")
        print("2.- No")
        Opcion = int(input(": "))

        if Opcion == 1:
            if Edad >= 18:
                print("Tu Edad es:",Edad,"eres MAYOR de Edad")
            else:
                print("Tu Edad es:",Edad,"eres MENOR de Edad")
        else:
            if Edad >= 18:
                print("Tu Edad es:",Edad-1,"eres MAYOR de Edad")
            else:
                print("Tu Edad es:",Edad-1,"eres MENOR de Edad")

    elif Menu == 4:
        ##Crear un Usuario
        lstUsuario = []

        print("----------------------------")
        Nombre = input("Dame su nombre: ")
        Edad = input("Dame su numero telefonico: ")
        Fecha_Nacimiento = input("Dame su fecha de nacimiento:")
        Color_Favorito = input("Dame su color favorito: ")
        print("----------------------------")

        lstUsuario.append(Nombre)
        lstUsuario.append(Edad)
        lstUsuario.append(Fecha_Nacimiento)
        lstUsuario.append(Color_Favorito)

        print("")
        print("Usuario registrado:",lstUsuario)
        
    elif Menu == 5:
        print("Vuelve pronto")
        break
    else:
        print("Valor ingresado no valido")