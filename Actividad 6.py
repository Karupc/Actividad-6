numeros = []
print("\n--MENÚ DE OPERACIONES MAFTEMÁTICAS--")
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
            numero = input(f"Ingrese el la cantidad {i+1}: ")
            numeros.append(numero)
        


