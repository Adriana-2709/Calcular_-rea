def calcular_area(base, altura):
    area = base * altura
    return area

b=float(input("Ingrese la base del rectángulo: "))
h=float(input("Ingrese la altura del rectángulo: "))

resultado = calcular_area(b, h)
print("El área del rectángulo es:", resultado)

    