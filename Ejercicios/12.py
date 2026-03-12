personas = 0

for i in range(5):
    nombre = input("Escriba su nombre: ")
    dias = int(input("Dias asistidos a la semana: "))
    horas = int(input("Horas de entrenamiento por dia: "))

    if dias < 3 :
        print("Bajo compromiso")
    elif dias >= 3  :
        print("Compromiso medio")
    else :
        print("Compromiso alto")    
