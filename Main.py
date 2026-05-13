volver = ""

print("===== SISTEMA DE NOTAS =====")

while volver != "no":

    nombre = input("\nIngrese el nombre del estudiante: ")

    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    nota4 = float(input("Ingrese la cuarta nota: "))
    nota5 = float(input("Ingrese la quinta nota: "))

    suma = 0

    notas = [nota1, nota2, nota3, nota4, nota5]

    for nota in notas:
        suma += nota

    promedio = suma / 5

    if promedio >= 4.5:
        print("Estado: Excelente")

    elif promedio >= 3.0:
        print("Estado: Aprobado")

    else:
        print("Estado: Reprobado")

    print("El promedio final de", nombre, "es", promedio)

    volver = input("¿Desea evaluar otro estudiante? (si/no): ")

    if volver == "no":
        print("Programa finalizado.")