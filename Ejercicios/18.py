bajos = 0
medios = 0
altos = 0
suma_grupo = 0
mejor_nota = 0
mejor_nombre = ""

estudiantes = int(input("¿Cuántos estudiantes? "))

for i in range(1, estudiantes + 1):
    nombre = input(f"\nNombre estudiante {i}: ")
    speaking = int(input("Nota speaking: "))
    listening = int(input("Nota listening: "))
    reading = int(input("Nota reading: "))

    promedio = (speaking + listening + reading) / 3
    print(f"Promedio: {promedio:.1f}")

    suma_grupo = suma_grupo + promedio

    if promedio < 60:
        print("Nivel: bajo")
        bajos = bajos + 1
    elif promedio < 80:
        print("Nivel: medio")
        medios = medios + 1
    else:
        print("Nivel: alto")
        altos = altos + 1

    if promedio > mejor_nota:
        mejor_nota = promedio
        mejor_nombre = nombre

promedio_grupo = suma_grupo / estudiantes

print(f"\nPromedio general: {promedio_grupo:.1f}")
print(f"Mejor estudiante: {mejor_nombre} con {mejor_nota:.1f}")
print(f"Nivel bajo: {bajos}")
print(f"Nivel medio: {medios}")
print(f"Nivel alto: {altos}")