contador = 0

for i in range(1, 7):
    precio = float(input(f"Precio producto {i}: "))
    if precio > 100000:
        contador += 1

print(f"Productos sobre $100.000: {contador}")
