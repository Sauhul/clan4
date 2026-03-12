cafe = 4000
capuchino = 7000
pastel = 6000
total = 0

opcion = 0

while opcion != 4:
    print("\n1. Café")
    print("2. Capuchino")
    print("3. Pastel")
    print("4. Salir")
    opcion = int(input("¿Qué desea? "))

    if opcion == 1:
        cantidad = int(input("¿Cuántos cafés? "))
        total += cafe * cantidad
        print(f"Subtotal: ${total}")
    elif opcion == 2:
        cantidad = int(input("¿Cuántos capuchinos? "))
        total += capuchino * cantidad
        print(f"Subtotal: ${total}")
    elif opcion == 3:
        cantidad = int(input("¿Cuántos pasteles? "))
        total += pastel * cantidad
        print(f"Subtotal: ${total}")
    elif opcion != 4:
        print("Opción no válida")

print(f"Total antes del descuento: ${total}")

if total > 20000:
    total = total * 0.9
    print("Descuento del 10% aplicado")

print(f"Total a pagar: ${total}")
print("Gracias por su visita")