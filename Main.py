volver = ""

print("Hola, Bienvenido.")

while volver != "no":

    nombre = input("Por Favor Ingrese su Nombre: ")

    nota1 = float(input(nombre + ", Ingrese su primera nota por favor: "))
    nota2 = float(input("Vale ahora Ingrese su segunda nota: "))
    nota3 = float(input("Ingrese su tercera nota: "))
    nota4 = float(input("Ingrese su cuarta nota: "))
    nota5 = float(input("Ingrese su quinta nota: "))

    suma = 0

    notas = [nota1, nota2, nota3, nota4, nota5]

    for nota in notas:
        suma += nota

    promedio = suma / 5

    if promedio >= 4.5:
        print("Excelente")

    elif promedio >= 3.0:
        print("Aprobado")

    else:
        print("Reprobado")

    print("El promedio de", nombre, "es de", promedio)

    volver = input("¿Desea evaluar a otro estudiante?: ")