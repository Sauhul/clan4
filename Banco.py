opcion = "0"
saldo =  0

while opcion != 4:
    print("========  Bienvenido al banco ===========")
    print("¿Qué operación deseas realizar?")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
    opcion = input("Selecciona una opción (1, 2, 3 o 4): ")

    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo}")
    elif opcion == "2":
        try:
            monto_retiro = input("Ingresa el monto a retirar: ") .replace(",", ".")
        except ValueError:
            print("Error: Debes ingresar un número válido.")
            continue
        if float(monto_retiro) > saldo:
            print("Fondos insuficientes. No se puede realizar el retiro.")
        else:
            saldo -= float(monto_retiro)
            print(f"Has retirado ${monto_retiro}. Tu nuevo saldo es: ${saldo}")
    elif opcion == "3":
        try:
            monto_deposito = input("Ingresa el monto a depositar: ") .replace(",", ".")
        except ValueError:
            print("Error: Debes ingresar un número válido.")
            continue
        saldo += float(monto_deposito)
        print(f"Has depositado ${monto_deposito}. Tu nuevo saldo es: ${saldo}")
    elif opcion == "4":
        print("Gracias por usar nuestros servicios. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

