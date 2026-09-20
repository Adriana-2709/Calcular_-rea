# Cálculo del área de un rectángulo

 **Nombre:** Adriana Almeida Aguilar
 **Institución:** Universidad Estatal Amazónica (UEA)

Programa en Python que calcula el área de un rectángulo usando una **función con parámetros y retorno de valores**.

## Problema que resuelve

Permite conocer la superficie de un objeto o espacio rectangular (un terreno, una mesa, una habitación) a partir de su base y su altura.

## Estructura del programa

- **Función:** `calcular_area(base, altura)`
- **Parámetros de entrada:** `base` y `altura`
- **Retorno:** devuelve el área con la palabra clave `return`
- **Llamada a la función:** `calcular_area(b, h)`
- **Salida:** el resultado se muestra en pantalla con `print`

## Código

```python
def calcular_area(base, altura):
    area = base * altura
    return area

b=float(input("Ingrese la base del rectángulo: "))
h=float(input("Ingrese la altura del rectángulo: "))

resultado = calcular_area(b, h)
print("El área del rectángulo es:", resultado)
```

## Cómo ejecutarlo

1. Instalar [Python 3](https://www.python.org/downloads/).
2. Descargar el archivo `calcular_area.py`.
3. Ejecutarlo desde la terminal:

```
python calcular_area.py
```

## Ejemplo de ejecución

```
Ingrese la base del rectángulo: 23.5
Ingrese la altura del rectángulo: 15
El área del rectángulo es: 352.5
```

## Video explicativo

[Ver video de programación](https://ueaeduec-my.sharepoint.com/:f:/g/personal/aa_almeidaa_uea_edu_ec/IgAvGiij1Z-4S6FfXKBqGagRAWubWJI0kai3p20qsZsETOc?e=Ep1xKd)

