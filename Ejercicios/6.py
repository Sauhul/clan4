hora1 = 5000
extra = 3000

print("Parking")
print("Ingrese la cantidad de horas que desea estacionar su vehículo:")
horas = int(input("Horas: "))   

if horas <= 0:
    print("Hora invalida")
elif horas == 1:
    print("Tu pago es de 5000")
else :
    total_a_pagar = (horas - 1) * 3000 + 5000 
    print(f"su total a pagar es de {total_a_pagar}")  
