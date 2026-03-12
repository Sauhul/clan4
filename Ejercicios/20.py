total = 0
basicos = 0
premiums = 0
familiares = 0

personas = int(input("¿Cuántas personas? "))

for i in range(1, personas + 1):
    nombre = input(f"\nNombre persona {i}: ")
    edad = int(input("Edad: "))
    plan = input("Plan (basico/premium/familiar): ")

    if edad < 18:
        print("Registro juvenil")
    elif edad >= 60:
        print("Beneficio senior")

    if plan == "basico":
        total = total + 50000
        basicos = basicos + 1
    elif plan == "premium":
        total = total + 90000
        premiums = premiums + 1
    elif plan == "familiar":
        total = total + 130000
        familiares = familiares + 1

print(f"\nTotal recaudado: ${total}")
print(f"Básico: {basicos}")
print(f"Premium: {premiums}")
print(f"Familiar: {familiares}")

if basicos >= premiums and basicos >= familiares:
    print("Plan más vendido: basico")
elif premiums >= familiares:
    print("Plan más vendido: premium")
else:
    print("Plan más vendido: familiar")