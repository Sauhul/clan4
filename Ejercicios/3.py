#ejjercicio 3
print("............Ejericio 3.............")

cafe = 4000
te = 3500
jugo = 5000

cafeteria = input("¿Desea comprar algo en la cafetería? (si/no): ")
if cafeteria.lower() == "si":
    print("Menú de la cafetería:")
    print("1. Café - $4000")
    print("2. Té - $3500")
    print("3. Jugo - $5000")
    
    opcion = input("Ingrese los productos que desea comprar (1, 2, 3): ")
    cantidad = int(input("Ingrese la cantidad que desea comprar: "))
   
    if opcion == "1":
       cafe_total = cafe * cantidad
       print(f"Has comprado  {cafe}${cafe_total}.")
           
    elif opcion == "2":
        
        te_total = te * cantidad
        print(f"Has comprado  {te} por ${te_total}.")
    elif opcion == "3":
        jugo_total = jugo * cantidad    
        print(f"Has comprado  {jugo} por ${jugo_total}.")
    else:
        print("Opción no válida. Por favor, elija un número entre 1 y 3.")
