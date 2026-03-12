total_alimento = 0
total_juguete = 0
total_accesorio = 0

for i in range(1, 11):
    categoria = input(f"\nVenta {i} - Categoría (alimento/juguete/accesorio): ")
    valor = int(input("Valor de la compra: "))

    if categoria == "alimento":
        total_alimento = total_alimento + valor
    elif categoria == "juguete":
        total_juguete = total_juguete + valor
    elif categoria == "accesorio":
        total_accesorio = total_accesorio + valor

print(f"\nAlimento: ${total_alimento}")
print(f"Juguete: ${total_juguete}")
print(f"Accesorio: ${total_accesorio}")

if total_alimento >= total_juguete and total_alimento >= total_accesorio:
    print("Categoría que más vendió: alimento")
elif total_juguete >= total_accesorio:
    print("Categoría que más vendió: juguete")
else:
    print("Categoría que más vendió: accesorio")