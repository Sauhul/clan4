total = 0
cortes = 0
cepillados = 0
tinturas = 0

for i in range(1, 8):
    nombre = input(f"\nNombre cliente {i}: ")
    servicio = input("Servicio (corte/cepillado/tintura): ")
    valor = int(input("Valor pagado: "))

    total = total + valor

    if servicio == "corte":
        cortes = cortes + 1
    elif servicio == "cepillado":
        cepillados = cepillados + 1
    elif servicio == "tintura":
        tinturas = tinturas + 1

print(f"\nTotal del día: ${total}")
print(f"Cortes: {cortes}")
print(f"Cepillados: {cepillados}")
print(f"Tinturas: {tinturas}")

if cortes >= cepillados and cortes >= tinturas:
    print("Servicio más solicitado: corte")
elif cepillados >= tinturas:
    print("Servicio más solicitado: cepillado")
else:
    print("Servicio más solicitado: tintura")