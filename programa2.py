'''
1) cambiar la linea 1 y que se ingrese el saldo inicial en teclado
2) cambiar el nombre de la variable saldo por saldoInicial
3)solo pueden depositar las personas que tienen saldo Inicial entre 1300 soles
hasta 9500 soles , las respuestas en soles y ingresos en soles


'''
saldoInicial = 1000

while True:
    print("\n--- Cajero Automático ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo}")
    elif opcion == "2":
        monto = float(input("Ingresa el monto a depositar: "))
        if monto > 0:
            #saldo += monto
            saldo = saldo + monto
            print(f"Has depositado ${monto}. Saldo actual: ${saldo}")
        else:
            print("Monto inválido.")
    elif opcion == "3":
        monto = float(input("Ingresa el monto a retirar: "))
        if 0 < monto <= saldo:
            saldo -= monto
            print(f"Has retirado ${monto}. Saldo actual: ${saldo}")
        else:
            print("Monto inválido o saldo insuficiente.")
    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
print("============= finalizo el progrma =================")