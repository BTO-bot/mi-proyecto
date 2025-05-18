# Python Fundamentals / Bucles for: Básico 1 (Core)
# Benjamin Rojas

# Ejercicio 1: Básico --- Imprimir todos los números enteros del 0 al 100
print("Ejercicio 1: Básico")
for i in range(101):
    print(i)


# Ejercicio 2: Múltiples de 2 --- Imprimir todos los múltiplos de 2 entre 2 y 500
print("Ejercicio 2: Múltiples de 2")
for i in range(2, 501, 2):
    print(i)


# Ejercicio 3: Contando Vanilla Ice
print("Ejercicio 3: Contando Vanilla Ice")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)


# Ejercicio 4: Wow. Número gigante a la vista --- Sumar los pares del 0 al 500,000
print("Ejercicio 4: Wow. Número gigante a la vista")
suma = 0
for i in range(0, 500001, 2):
    suma += i
print("La suma total es:", suma)


# Ejercicio 5: Regrésame al 3 --- Cuenta regresiva de 3 en 3 desde 2024
print("Ejercicio 5: Regrésame al 3")
for i in range(2024, 0, -3):
    print(i)


# Ejercicio 6: Contador dinámico
print("Ejercicio 6: Contador dinámico")
numInicial = 3
numFinal = 10
multiplo = 2
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)