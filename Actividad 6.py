numeros = []
print("\n--MENÚ DE OPERACIONES MAFTEMÁTICAS--\n")
print("1.- Ingresar números y mostrar\n"
      "2.- Calcular el área de un triángulo\n"
      "3.- Verificar si un número es par o impar\n"
      "4- Calcular el promedio de calificaciones\n"
      "5.- Ingresar números y mostrar el mayor y menor\n"
      "6.- Salir del programa")
opciones = input("Ingrese el número de la opción que desea seleccionar: ")
match opciones:
    case "1":
        cantidad = int(input("¿Cuántos números desea ingresar?: "))
        for i in range(cantidad):
            numero = int(input(f"Ingrese el la cantidad {i+1}: "))
            numeros.append(numero)
        while True:
            print("\n--ELIJA LO QUE DESEA VER--\n"
                  "1.- La suma total\n"
                  "2.- El promedio\n"
                  "3.- La cantidad de números positivos y negativos\n"
                  "4.- Salir")
            opciones2 = input("Escriba el número de la opción que elige: ")
            match opciones2:
                case "1":
                    def suma_total():
                        suma = sum(numeros)
                        print(f"La suma total es: {suma}")
                    suma_total()
                case "2":
                    def promedio():
                        prom = sum(numeros) / len(numeros)
                        print(f"El promedio es: {prom}")
                    promedio()
                case "3":
                    positivos = 0
                    negativos = 0
                    for num in numeros:
                        if num > 0:
                            positivos += 1
                        elif num < 0:
                            negativos += 1
                    print(f"Cantidad de números positivos: {positivos}")
                    print(f"Cantidad de números negativos: {negativos}")
                case "4":
                    print("Volverá al primer menú")
                    break

