

print("elija su sabor de helado")
print("1. Vainilla")
print("2. Chocolate")
print("3. Fresa")   
sabor = input("Ingrese el número del sabor que desea: ")
helados = int(input("Ingrese la cantidad de helados que desea: "))

while helados > 5:
        print("No se pueden pedir más de 5 helados.")
        helados = int(input("Ingrese la cantidad de helados que desea: "))

if sabor == "1":
    print("Has elegido Vainilla")
elif sabor == "2":
    print("Has elegido Chocolate")
elif sabor == "3":
    print("Has elegido Fresa")
else:
    print("Opción no válida. Por favor, elija un número entre 1 y 3.")