capacidad = int(input("Capacidad de la sala: "))
ninos = 0
adultos = 0
mayores = 0

for i in range(capacidad):
    edad = int(input(f"Edad persona {i + 1}: "))

    if edad < 12:
        ninos += 1
    elif edad <= 59:
        adultos += 1
    else:
        mayores += 1

total = ninos + adultos + mayores

print(f"\nTotal ingresados: {total}")
print(f"Niños: {ninos}")
print(f"Adultos: {adultos}")
print(f"Adultos mayores: {mayores}")

if total == capacidad:
    print("La sala se llenó")
else:
    print("La sala no se llenó")