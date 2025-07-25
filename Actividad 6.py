numeros = []
notas = []
numeros2 = []
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
    case "2":
         print("\n--CALCULAR EL ÁREA DE UN TRIÁNGULO--\n")
         base = int(input("Ingrese la base del triángulo en cm: "))
         altura = int(input("Ingrese la altura del triángulo en cm: "))
         def area_triangulo(base, altura):
             print("El área del triángulo es de: ", (base * altura) / 2, "cm")
         area_triangulo(base, altura)
    case "3":
         print("\n--VERIFICAR SI UN  NÚMERO ES PAR O IMPAR--")
         numero = int(input("Ingrese un número: "))
         def numero_par_impar(numero):
             if numero % 2 == 0:
                 print(f"{numero} es par")
             else:
                 print(f"{numero} es impar")
         numero_par_impar(numero)
    case "4":
        cursos = int(input("Ingrese la cantidad de cursos que tiene: "))
        for i in range(cursos):
            nota = int(input(f"Ingrese la nota del curso {i+1}: "))
            notas.append(nota)
        def promedio_cursos():
            prome = sum(notas) / len(notas)
            print(f"El promedio es de {prome}")
        promedio_cursos()
    case "5":
        n = int(input("¿Cuántos números desea ingresar?: "))
        for i in range(n):
            num = int(input(f"Ingrese el número {i+1}: "))
            numeros2.append(num)
        def num_mayor_menor():
            nma = max(numeros2)
            nme = min(numeros2)
            print(f"El número mayor es: {nma}")
            print(f"El número menor es: {nme}")
        num_mayor_menor()