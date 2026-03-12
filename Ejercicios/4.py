#ejercicio 4
print("............Ejericio 4.............")
print("Taquilla de cine")
print("1. Niño (0-12 años) - $8000")
print("2. Adulto (13-59 años) - $12000")
print("3. Adultos mayores (60+ años) - $9000")
edad = int(input("Ingrese su edad: "))
if edad < 13:
    print("Has elegido la categoría Niño. El precio es $8000.")
elif edad >= 13 and edad < 60:
    print("Has elegido la categoría Adulto. El precio es $12000.")
else:
    print("Has elegido la categoría Adultos mayores. El precio es $9000.")