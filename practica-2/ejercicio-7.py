# Pedir al usuario dos números de punto flotante
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Calcular el promedio
promedio = (numero1 + numero2) / 2

# muestro el promedio
print("El promedio es:", promedio)

# Decidir si aprobo o desaprobo
if promedio > 7:
    print("Aprobado")
else:
    print("Desaprobado")
