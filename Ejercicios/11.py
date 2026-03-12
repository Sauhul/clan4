total = 0
clientes = 0
conos = 0
vasos = 0
bananas = 0

opcion = input("¿Atender cliente? (si/no): ")

while opcion == "si":
    producto = input("Producto (cono, vaso, banana split): ")
    cantidad = int(input("Cantidad: "))

    if producto == "cono":
        total += 3000 * cantidad
        conos += cantidad
    elif producto == "vaso":
        total += 4000 * cantidad
        vasos += cantidad
    elif producto == "banana split":
        total += 9000 * cantidad
        bananas += cantidad

    clientes += 1
    opcion = input("¿Atender otro cliente? (si/no): ")

print(f"Total vendido: ${total}")
print(f"Clientes atendidos: {clientes}")

if conos >= vasos and conos >= bananas:
    print("Producto más pedido: cono")
elif vasos >= bananas:
    print("Producto más pedido: vaso")
else:
    print("Producto más pedido: banana split")