total = 0
carros = 0
motos = 0
max_pago = 0
placa_max = ""

for i in range(1, 9):
    placa = input(f"Placa del vehículo {i}: ")
    tipo = input("Tipo (carro/moto): ")
    horas = int(input("Horas parqueado: "))

    if tipo == "carro":
        pago = 4000 * horas
        carros = carros + 1
    elif tipo == "moto":
        pago = 2000 * horas
        motos = motos + 1

    total = total + pago

    if pago > max_pago:
        max_pago = pago
        placa_max = placa

print(f"Total recaudado: ${total}")
print(f"Carros: {carros}")
print(f"Motos: {motos}")
print(f"Vehículo que más pagó: {placa_max} con ${max_pago}")