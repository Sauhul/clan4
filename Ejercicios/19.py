agotados = 0
bajos = 0
normales = 0

for i in range(1, 11):
    nombre = input(f"\nNombre producto {i}: ")
    cantidad = int(input("Cantidad disponible: "))

    if cantidad == 0:
        print("Agotado")
        agotados = agotados + 1
    elif cantidad <= 5:
        print("Stock bajo")
        bajos = bajos + 1
    else:
        print("Stock normal")
        normales = normales + 1

print(f"\nAgotados: {agotados}")
print(f"Stock bajo: {bajos}")
print(f"Stock normal: {normales}")