# Algoritmo repetitivo con while: Sumar números hasta que el usuario ingrese 0

suma = 0

# Bucle while: Se repite mientras el número no sea 0
numero = float(input("Ingresa un número (0 para salir): "))

while numero != 0:
    suma += numero  # Acumular la suma
    numero = float(input("Ingresa otro número (0 para salir): "))

# Salida
print(f"La suma total es: {suma}")
