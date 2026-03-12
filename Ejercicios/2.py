#ejercicio 2


print("............Ejericio 2.............")

print("Ingrese su edad")
edad = int(input("Edad: "))

if edad <13:
    print("No puedes ingresar")
elif edad >= 13 and edad < 17:
    print("Clase juvenil")
elif edad >= 18 and edad < 59:
    print("Clase adulta")
else:    
    print("Clase senior")
